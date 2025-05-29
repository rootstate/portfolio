$(function () {
    // hit the API, right now absolute path because page origin is port 3000 and fastAPI orogin is 8000
    $.get("http://localhost:8000/api/counter")     
      .done(function (data) {                      
        $("#visitCount").text(data.visits);        // drop it in the span
      })
      .fail(function () {                          // basic fallback
        $("#visitCount").text("--");
      });
  });
  