var p = $('#ab');
// while(0){
// p.toggle(3000);
// } 
var jqxhr = $.getJSON('/api/',{
    dataType: 'json'
}).done(function (data) {
    // data已经被解析为JSON对象了
});