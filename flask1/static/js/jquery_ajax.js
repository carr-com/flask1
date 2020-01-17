$("document").ready(function(){
    function ajax_login(){
        $.ajax({
            url: "/ajax-login",
            data: $('form').serialize(),
            type: "POST",
            success: function(response) {
            console.log(response);
            },
            error: function(error) {
                alert("error: " + error.status);
                console.log(error);
            }
        });
    }

    $('#LoginAjax').submit(function(event) {
        event.preventDefault();
        ajax_login();
    });

});

