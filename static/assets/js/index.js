// $(document).ready(function() {
    $("#comment").submit(function(e) {
        e.preventDefault(); 
        
        // Serialize the form data.
        var formData = $(this).serialize();
        var method = $(this).attr("method");
        var url = $(this).attr("action");

        // Make an AJAX request.
        $.ajax({
            dataType: "json",
            url: url,
            data: formData,
            method: method,
            success: function(response) {
                console.log("Success");
            },
            error: function(error) {
                console.log("Error");
            }
        });
    });
// });
