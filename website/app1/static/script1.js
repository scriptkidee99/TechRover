console.log('load script 3');
// alert('load 1')



///////////////////////////////////////////////////////////////



var display = false;

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
    console.log('selected');
    if (document.getElementById('logIn').checked) {
        // $('logInContent').show();
        document.getElementById('logInContent').style.display = "block";
        // $('signUpContent').hide();
        document.getElementById('signUpContent').style.display = "none";
        console.log('Log In');
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
$(document).ready(function(){
    $('#logIn').prop('checked' ,'true');    
})

$(document).ready(function() {
    $("#logInButton").click(function() {
        console.log("Log In Button Clicked");
        if ($("#userState").text() != "check")
        {
            console.log("show sign options");
           $(".sign").show();
    }
    else{
        console.log("sign out");
        $("#logOutForm").submit();
    }
    });
    $(".signCloseButton").click(function() {
        $(".sign").hide();
    });
    $("#profile").click(function() {
        $("#profile_menu").show();
    });
    $("#profileEdit").click(function(){
        $("#profile_menu").show();
    })
})

function cl() {
    alert('yep right');
}




$('document').ready(function(){
    $('.blog_img').click(function(){
        $('.fullImgPicker').click();
    });
})

$('document').ready(function(){
    $('.fullImgPicker').change(function(){
        //('.blog_img').attr('src','')
        console.log($('.fullImgPicker').val());
        $('#imgform').submit();
    })
})


$('document').ready(function(){
    $(".card").on("click", function() {
        $(this).submit();
    });
    $('.cardEdit').on("click",function(){
        $(this).submit();
    });
})


$(document).ready(function(){
    //var userStateText = $("$userState").text();
    if (($("#userState").text()) == "notFound"){
        alert("User does not exist. Try signing up");
    }
    else if(($("#userState").text()) == "mismatch"){
        alert("Username password mismatch");
    }
})


$(document).ready(function(){
    $('#heart').on("click",function(){
        if($('#profile').val() != 'U'){
            $('#heart').toggleClass("heartFilled");
            var classValue = $('#heart').attr('class');
            if(classValue.includes('heartFilled')){
                $('.heartCheck').prop('value','True');
            }
            else{
                $('.heartCheck').prop('value','False');
            }
            $('#setFavorite').submit();
    }
    else{
        alert("Yoy need to sign in to use this feature");
    }
    });
})


$(document).ready(function(){
    if($('.heartCheck').prop('value') == 'True'){
        $('#heart').addClass('heartFilled');
    }
    else{
        $('#heart').removeClass('heartFilled');
    }
})
