$(document).ready(function () {

    console.log("JavaScript connected");

    $("#contactForm").submit(function (e) {
        e.preventDefault();

        let name = $("#name").val().trim();
        let email = $("#email").val().trim();

        if (name === "" || email === "") {
            alert("Please fill all required fields");
        } else {
            $("#success").removeClass("d-none");
            $(this)[0].reset();
        }
    });

});
