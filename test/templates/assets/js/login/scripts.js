
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("assets/img/backgrounds/1.jpg");
    
    /*
        Form validation
    */
    // $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
    // 	$(this).removeClass('input-error');
    // });
    
    $('.login-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function(){
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
                $(this).removeClass('input-error');
                login();
    		}
    	});
    });

    // $('.main-title').on('click', function() {
    //     login();
    // })

});

function login() {
    username = $('.login-form input[type="text"]').val();
    password = $('.login-form input[type="password"]').val();
    $.ajax({
        url: 'http://localhost:9090/Login',
        data: {
            'username': username,
            'password': password
        },
        type: 'POST',
        success: function(res) {
            alert(JSON.stringify(res));
            window.location.href = '/index.html';
        },
        error: function(err) {
            alert('登录失败');
        }
    });
}
