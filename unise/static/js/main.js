/*
<div class="link">
    <p class="title">Dispensa Resto.pdf <br>
        <span class="path">C:/Users/marco/Desktop/prova_template/index.html</span>
    </p>

    <p class="snippet"></p>
</div>
*/


// SEARCH
$("#search_button").on("click", function(){
    search();
});

$(document).on('keypress', function(event) {
    let keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13') {
        search();
    }
});

function search() {
    $(".search_output").find("div").remove();
    $(".search_output img").css("display", " block");

    $.ajax({
        data : {
            keyword: $("#keyword").val(),
            sort: $('input[name="sort"]:checked').val(),
            limit: $("#limit").val(),
        },
        type : 'POST',
        url : '/search'
    })
    .done(function(data) {
        $(".search_output img").css("display", "");
        fill(data);
    });
}

function fill(data){
    $(".search_output").find("div").remove();
    for(var i = 0; i<data.length; i++){
        $(".search_output").append("<div class='link'><p class='title'>"+data[i].title+"<br><span class='path'>"+data[i].path+"</span></p>");
    }
    $("#contatore span").text(data.length);
}

// OPEN FILE
$(".search_output").on("click", ".title", function(){
    console.log($(this).children(".path").text());
    $.ajax({
        data : {
            path: $(this).children(".path").text()
        },
        type : 'POST',
        url : '/visual'
    })
    .done(function(data) {
        console.log(data)
        console.log("visualized")
    });
})