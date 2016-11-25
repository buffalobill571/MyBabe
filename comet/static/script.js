$(document).ready(function() {
  var source = new EventSource("new/");
  source.onmessage = function(event) {
    $("img#smth").animate({
        left: '+=250px',
        height: '+=150px',
        width: '+=250px',
        opacity: 1
    }, 1500);
    $("img#smth").attr({
      src: event.data,
    });
    $("img#smth").animate({
        left: '-=250px',
        height: '-=150px',
        width: '-=250px',
        opacity: 0
    }, 1500);
  };
});
