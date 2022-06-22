function validatePassword() {

    var value = document.getElementById('password').value;
    const pattern = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;
    if (!pattern.test(value)) {
        var element = document.getElementById('password-error');
        element.innerHTML = 'Password must contain at least 8 characters';
        element.style.visibility = 'visible';

    } else {
        var element = document.getElementById('password-error');

        element.style.visibility = 'hidden';

    }



}

function validateConfirmPassword() {

    var value = document.getElementById('confirm-password').value;
    const pattern = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;
    if (!pattern.test(value)) {
        var element = document.getElementById('confirm-password-error');
        element.innerHTML = 'Password must contain at least 8 characters';
        element.style.visibility = 'visible';

    } else {
        var element = document.getElementById('confirm-password-error');

        element.style.visibility = 'hidden';

    }



}

function matchPasswords() {

    var value1 = document.getElementById('confirm-password').value;
    var value2 = document.getElementById('password').value;
    console.log(value1);
    console.log(value2);

    if (!(value1 == value2)) {
        var element = document.getElementById('confirm-password-error');
        element.innerHTML = 'Passwords should be same';
        element.style.visibility = 'visible';

    } else {
        var element = document.getElementById('confirm-password-error');
        element.innerHTML = '';
        element.style.visibility = 'hidden';

    }



}