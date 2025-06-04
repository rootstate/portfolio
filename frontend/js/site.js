$(function () {
    $.get("/api/counter/")     
      .done(function (data) {                      
        $("#visitCount").text(data.visits);        // drop it in the span
      })
      .fail(function () {                          // basic fallback
        $("#visitCount").text("NaN");
      });
  });