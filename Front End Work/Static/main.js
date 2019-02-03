console.log("MAIN JS")

$('#fin').on('click', function(e) {
  // gather all checked radio-button values
  var choices = $("input[type='radio']:checked").map(function(i, radio) {
    return $(radio).val();
  }).toArray();
  fetch('http://localhost/quiz', {method: 'POST', body: JSON.stringify(choices)}).then(res => {
    const spotifyId = res.body;
  })
  var mood = ["happy", "calm", "angry", "sad"];
  var key;

  if (choices.length >=4) {
    $('button[type=calculate]').css("display", "none");
    var count = 0;
    for (i = 0; i < choices.length; i++) {
      count += parseInt(choices[i]);

    }
    if (count > 18) {
      $('#happy').css("display", "block");
      key = mood[0];
    }
    else if (count > 14) {
      $('#mellow').css("display", "block");
      key = mood[1];
    }
    else if (count > 9) {
      $('#angry').css("display", "block");
      key = mood[2];
    }
    else {
      $('#sad').css("display", "block");
      key = mood[3];
    }
  }
  $.ajax({
            type: "POST",
            contentType: "application/json;charset=utf-8",
            url: "http://localhost:5000/quiz",
            traditional: "true",
            data: JSON.stringify({key}),
            dataType: "json"
            });

});

$("input[type='radio']").on('change', function (e) {
  $('.results').css("display", "none");
  $('#error').css("display", "none");
  $('button[type=calculate]').css("display", "block");

  var checked = $(this).attr('id'); // http://stackoverflow.com/questions/15141530/get-text-of-label-that-belongs-to-checked-radio-button
  var group = $(this).attr('name');

  $(`div[type=${group}]`).css("opacity", ".6");
  $(`div[type=${group}]`).css("background", "rgba(220, 220, 220, 1)");
  $(`div[type=${group}]`).css("box-shadow", "0em 0em 0em 0em rgba(50, 50, 50, 1)");

  $(`#${checked}`).css("opacity", "1");
  $(`#${checked}`).css("background", "rgba(187, 200, 255, 1)");
  $(`#${checked}`).css("box-shadow", "0em 0em .9em .2em rgba(50, 50, 50, 1)");
});
