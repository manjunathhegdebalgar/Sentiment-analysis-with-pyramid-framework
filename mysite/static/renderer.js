$(document).ready(function () {
    $("#review").change(function () {
        var newValue = $("#review").val();
        // Passing the data fetched from the input box as a Json to the app
        $.ajax({
            method: "POST",
            url: "/",
            data: JSON.stringify({review: newValue}),
            contentType: 'application/json; charset=utf-8'
        }).done(
            function (data) {
            /* Following lines are intended to get the information in the response and append to strings
                so that they are rendered in a better way to the user. */
                var emotion = data.sentiment
                var probability = data.probability
                var starting_response_string = "The review is classified as "
                var response_string_with_emotion = starting_response_string.concat(emotion)
                var middle_response_string = response_string_with_emotion.concat(" by our engine with the confidence of ")
                // final response contains the message shown to the user.
                var pre_final_response = middle_response_string.concat(probability)
                var final_response = pre_final_response.concat("%")
                $('#printingplace').text(final_response);
            }
        );
    });
})
;
