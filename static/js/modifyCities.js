$(document).ready(function () {
    /* CARGA QUERY MODAL (MATERIALIZE CSS)*/
    $('.modal').modal();

    /* AJAX MOSTRAR DATOS EN COLECCION O LISTA PARA ACTUALIZAR Y BORRAR*/
    $.ajax({
        type: "POST",
        url: "/ajaxAllCities",
        success: function (response) {
            response = JSON.parse(response);
            html = []
            for (let i = 0; i < response.length; i++) {
                html.push(`<li id="`+response[i].ID+`" class="collection-item">`+response[i].NAME+`<a class="delete" href="#"><i class="material-icons right red-text">cancel</i></a><a href="#modalData" class="update modal-trigger"><i class="material-icons right red-text">sync</i></a></li>`)
                }
                document.getElementById("cityCollection").innerHTML = html.join("");
        }
    });

    /* BORRAR DATOS DE FORMULARIO EN CREACION DE CIUDAD*/
    $("#createCity").click(function (e) { 
        $("#i_idCity").val("");
        $("#i_nameCity").val("");
        $("#i_countryCode").val("");
        $("#i_districtCity").val("");
        $("#i_populationCity").val("");
    });

    /* ACCION GUARDAR DATOS PARA CREACION DE CIUDAD*/
    $("#b_saveCity").click(function (e) { 
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/CreateCity",
            data: {
                "NAME": $("#i_nameCity").val(),
                "COUNTRYCODE": $("#i_countryCode").val(),
                "DISTRICT": $("#i_districtCity").val(),
                "POPULATION": $("#i_populationCity").val()
            },
            success: function (response) {
                html = `<li id="`+$("#i_idCity").val()+`" class="collection-item">`+$("#i_nameCity").val()+`<a class="delete" href="#"><i class="material-icons right red-text">cancel</i></a><a href="#modalData" class="update modal-trigger"><i class="material-icons right red-text">sync</i></a></li>`;
                $("#cityCollection").append(html);
                alert(response);
                $("#i_idCity").val("");
                $("#i_nameCity").val("");
                $("#i_countryCode").val("");
                $("#i_districtCity").val("");
                $("#i_populationCity").val("");
            }
        });
    });

    /* BORRAR ELEMENTOS DE COLECCION O LISTA*/
    $(document).on("click","a", function (e) {
        e.preventDefault();
        var btnName = $(this).attr("class");
        var id = $(this).closest('li').attr('id');
        if (btnName == "delete") {
            document.getElementById(id).remove()
            $.ajax({
                type: "POST",
                url: "/deleteCity",
                data: {
                    "id": id
                },
                success: function (response) {
                    alert(response);
                }
            });
        }
    
        /* ACTUALIZAR ELEMENTOS DE COLECCION O LISTA */
        else if (btnName == 'update modal-trigger'){
            $.post("/seachCityById", {"id":id},
                function (response) {
                    response = (JSON.parse(response));
                    $("#i_idCity").val(response.ID);
                    $("#i_nameCity").val(response.NAME);
                    $("#i_countryCode").val(response.COUNTRYCODE);
                    $("#i_districtCity").val(response.DISTRICT);
                    $("#i_populationCity").val(response.POPULATION);
                }
            );
            $("#formData").submit(function (e) { 
                e.preventDefault();
                $.ajax({
                    type: "POST",
                    url: "/UpdateCity",
                    data: {
                        "ID":$("#i_idCity").val(),
                        "NAME":$("#i_nameCity").val(),
                        "COUNTRYCODE":$("#i_countryCode").val(),
                        "DISTRICT":$("#i_districtCity").val(),
                        "POPULATION":$("#i_populationCity").val()
                    },
                    success: function (response) {
                        alert(response);
                        $("#i_idCity").val("");
                        $("#i_nameCity").val("");
                        $("#i_countryCode").val("");
                        $("#i_districtCity").val("");
                        $("#i_populationCity").val("");
                    }
                });
            });
        }
    });
});