$(() => {
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        type: "GET",
        success: (data) => {
            //console.log(data);
            $("#character").text(data.name);
        }
    })
})
