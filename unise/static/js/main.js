/*
<div class="link">
    <p class="title">Dispensa Resto.pdf <br>
        <span class="path">C:/Users/marco/Desktop/prova_template/index.html</span>
    </p>

    <p class="snippet"></p>
</div>
*/


$("#search_button").on("click", function(){

    $.ajax({
        data : {
            keyword: $("#keyword").val(),
            sort: $('input[name="sort"]:checked').val()
        },
        type : 'POST',
        url : '/search'
    })
    .done(function(data) {
        fill(data);
    });

});

function fill(data){
    $(".search_output").empty();
    for(var i = 0; i<data.length; i++){
        $(".search_output").append("<div class='link'><p class='title'>"+data[i].title+"<br><span class='path'>"+data[i].path+"</span></p>");
    }
}

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
        console.log("visualized")
    });
})