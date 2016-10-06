
$('select').on('change', function() {
    console.log();
    if (this.value) {
        $('#submit_button').prop('disabled', false);
    }else{
        $('#submit_button').prop('disabled', true);
    };
});

var cities = [];

if (!$.isEmptyObject(data)) {
    data.forEach(function(element, index, array) {
        var obj = {name:data[index].fields.name, data:[parseInt(data[index].fields.data)]};
        cities.push(obj);
    });
};


var chartOpt = {
        chart: {
            renderTo: 'chart',
            type: 'column'
        },
        title: {
            text: 'Данные по районам'
        },
        subtitle: {
            text: 'Источник: CSV файл'
        },
        xAxis: {
            categories: [region],
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Значение'
            }
        },
        legend: {
            enabled: true
        }

    };

chartOpt.series=cities;


$(function () {
    var myChart = Highcharts.chart(chartOpt);
});
