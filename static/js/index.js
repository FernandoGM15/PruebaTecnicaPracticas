$(document).ready(function () {

    /* AJAX MOSTRAR DATOS EN GRAFICA*/
    $.ajax({
        type: "POST",
        url: "ajaxChart",
        success: function (response) {
            Highcharts.chart('chart', {
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false,
                    type: 'pie'
                },
                title: {
                    text: 'POPULATION BY COUNTRY'
                },
                series: [{
                    name: 'Brands',
                    colorByPoint: true,
                    data: JSON.parse(response)
                }]
            });
        }
    });

    /* AJAX MOSTRAR DATOS 5 CIUDADES MAS POBLADAS*/
    $.ajax({
        type: "POST",
        url: "ajaxMostPopulated",
        success: function (response) {
            response = JSON.parse(response);
            for (let i = 0; i < response.length; i++) {
                $("#MostPopulatedCities").append(
                    `
                    <tr>
                        <td>`+response[i].ID+`</td>
                        <td>`+response[i].NAME+`</td>
                        <td>`+response[i].COUNTRYCODE+`</td>
                        <td>`+response[i].DISTRICT+`</td>
                        <td>`+response[i].POPULATION+`</td>
                    </tr>
                    `
                );
            }
        }
    });

    /* AJAX MOSTRAR DATOS TODAS LAS CIUDADES*/
    $.ajax({
        type: "POST",
        url: "ajaxAllCities",
        success: function (response) {
            response = JSON.parse(response);
            html = [];
            for (let i = 0; i < response.length; i++) {
                html.push(`
                    <tr class = "scrolltr">
                        <td>`+response[i].ID+`</td>
                        <td>`+response[i].NAME+`</td>
                        <td>`+response[i].COUNTRYCODE+`</td>
                        <td>`+response[i].DISTRICT+`</td>
                        <td>`+response[i].POPULATION+`</td>
                    </tr>
                    `)
            }
            document.getElementById("allCities").innerHTML = html.join("");
        }
    });
});