var display = false;
document.getElementById('logInButton').checked = true;
 
function myFunction(x) {

    var margin = 50;
    x.classList.toggle("change");
    menu_bar = document.getElementById("menu_bar");
    namePlate = document.getElementById("namePlate");
    if (display) {
        display = !display;

        var width = 136;
        menu_bar.style.width = width;

        var id = setInterval(hide_slowly, 0.05);

        function hide_slowly() {

            if (width <= 0) {
                clearInterval(id);
            } else {
                width -= 1.36;
                menu_bar.style.width = width;
            }
        }



    } else {
        display = !display;
        menu_bar.style.display = "block";


        var width = 0;
        menu_bar.style.width = width;

        var id = setInterval(show_slowly, 0.1);

        function show_slowly() {

            if (width >= 136) {
                clearInterval(id);
            } else {
                width += 1.36;
                menu_bar.style.width = width;
            }
        }

    }


}

// var display_profile_menu = true;

// function show_profile() {

//     if (display_profile_menu) {
//         document.getElementById("profile_menu").style.display = "block";
//     } else {
//         document.getElementById("profile_menu").style.display = "none";
//     }
//     display_profile_menu = !display_profile_menu;

// }



function checkToLoad() {
    console.log('selected it');
    if (document.getElementById('logIn').checked) {
        // $('logInContent').show();
        document.getElementById('logInContent').style.display = "block";
        // $('signUpContent').hide();
        document.getElementById('signUpContent').style.display = "none";
    } else {
        console.log('Sign Up');
        // $('logInContent').hide();
        // console.log("It is ", document.getElementById('logInContent'));
        document.getElementById('logInContent').style.display = "none";
        // $('signUpContent').show();
        document.getElementById('signUpContent').style.display = "block";
    }

}


$(document).mouseup(function(e) {
    if ($(e.target).closest("#profile_menu").length ===
        0) {
        $("#profile_menu").hide();
    }
});


$(document).ready(function() {
    $("#logInButton").click(function() {
        $(".sign").show();
    });
    $(".signCloseButton").click(function() {
        $(".sign").hide();
    });
    $("#profile").click(function() {
        $("#profile_menu").show();
    });
    $(".card").on("click", function() {
        $(this).submit();
    });
    
})


// $("document").ready(function() {
//     $(".card").on("click", function() {
//         $(this).submit();
//     });
// })

$(document).ready(function(){
    var text = $("#userState");
    console.log("The user state is ",text);
})