console.log('load script 4');
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
        $('#menu_bar').css('width',136);
        $('.mbcontent').fadeOut(200);    
        $('#menu_bar').delay(200).animate({
            width:0
            
        },1000)
        
    } else {
        display = !display;
        menu_bar.style.display = "block";


        var width = 0;
        menu_bar.style.width = width;

        $('#menu_bar').animate({
            width:136
        },1000,function(){
            $('.mbcontent').fadeIn(300);    
        });

        
        
        

        

    }

}



function checkToLoad() {
    console.log('selected');
    if (document.getElementById('logIn').checked) {
        document.getElementById('logInContent').style.display = "block";
        document.getElementById('signUpContent').style.display = "none";
        console.log('Log In');
    } else {
        console.log('Sign Up');
        document.getElementById('logInContent').style.display = "none";
        document.getElementById('signUpContent').style.display = "block";
    }

}


$(document).mouseup(function(e) {
    if ($(e.target).closest("#profile_menu").length ===
        0) {
        $("#profile_menu").hide();
    }
});
$(document).ready(function(){$('#logIn').prop('checked' ,'true');})

$(document).ready(function() {
    $("#logInButton").click(function() {
        console.log("Log In Button Clicked");
        if($('#profile').val() == 'U'){
        $(".sign").show();
        $('#unameBox').focus();
    }
    else{
        $('#logOutForm').submit();
    }

    });
    $(".signCloseButton").click(function() {
        $(".sign").hide();
    });
    $("#profile").click(function() {
        $("#profile_menu").show();
    });
    $("#profileEdit").click(function() {
        $("#profile_menu").show();
    });

})

function cl() {
    alert('yep right');
}


$('document').ready(function() {
    $('#namePlate').click(function() {
        
    })
})

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
    $('#screen').css('height','1px');
    $('#screen').css('margin-top','500px');
    $('#screen').css('opacity',0.5);
    $('.row').hide();
    $('#screen').animate({
        height:500,
        marginTop:50,
        opacity:1

    },1000,function(){
        $('.row').delay(300).fadeIn(1000);
    });
})


$(document).ready(function(){
    $('#savedButton').click(function(){
        if($('#profile').val() != 'U')
        {
            document.location.href = "http://127.0.0.1:8000/favorite";
        }
        else{
            alert('You need to log in to use this feature');
        }
    })
})


// $(document).ready(function(){
//     $("#signUpButton").on("click",function(){
//         var fname,lname,email,password='default';
//         if( ! $('#emailBox').prop('disabled')){
//             fname = $('#fNameBox').val();
//             lname = $('#lNameBox').val();
//             email = $('#emailBox').val();
//             password = $('#passwordBox').val(); 
//             console.log('Password is ',password);
//             alert('Re-enter password to confirm it');
//             $('#fNameBox').prop('disabled',true);
//             $('#lNameBox').prop('disabled',true);
//             $('#emailBox').prop('disabled',true);
//             $('#passwordBox').val('');
//             $('#passwordBox').focus();
//         }
//         else{
//             var cpassword = $('#passwordBox').val(); 
//             console.log('confirm is ',password);
//             if(password == cpassword)
//             {
//                 $('#signUpContent').submit();
//             }
//             else{
//                 alert('Password did not match as ',password,' ',cpassword);
//                 $('#fNameBox').prop('disabled',false);
//                 $('#lNameBox').prop('disabled',false);
//                 $('#emailBox').prop('disabled',false);
//                 $('#passwordBox').val('');
//                 $('#passwordBox').focus();
//             }
//         }
//     });
// })



$(document).ready(function(){
    $('#passwordBox').on('input',function(){
        var password = $('#passwordBox').val();
        var strength = 0;
        var length = password.length;
        if(length>=1 && length<=7) strength += 1;
        if(length>=8) strength += 2;
        if(/\d/.test(password)) strength += 1;
        console.log(strength);
        $('#passmeter').val(strength);
        if(strength == 0) $('#passmeterText').text('');
        else if(strength == 1) $('#passmeterText').text('weak');
        else if(strength == 2) $('#passmeterText').text('medium');
        else $('#passmeterText').text('strong');

    });
    $('#confirmPasswordBox').on('input',function(){
        if($('#passwordBox').val() == $('#confirmPasswordBox').val()){
            $('#passwordBox').css('border','2px solid green');
            $('#confirmPasswordBox').css('border','2px solid green');
        }
        else{
            $('#passwordBox').css('border','1px darkblue solid');
            $('#confirmPasswordBox').css('border','2px solid red');   
        }
    })
})

$(document).ready(function(){
    $('#signUpButton').click(function(){
        var fname = $('#fNameBox').val();
        var lname = $('#lNameBox').val();
        var email = $('#emailBox').val();
        var password = $('#passwordBox').val();
        var cpassword = $('#confirmPasswordBox').val();
        if (password == cpassword){
            $('#signUpContent').submit();
        }
    })
})