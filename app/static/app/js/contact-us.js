var data = document.getElementById('comment');
var userEmail = document.getElementById('email');
console.log(userEmail);

function sendEmail() {
    Email.send({

            Host: "smtp.gmail.com",
            Username: "Librarymanagementsystem.demo@gmail.com",
            Password: "Qwerty123@",
            To: userEmail,
            From: "Librarymanagementsystem.demo@gmail.com",
            Subject: "Thanks for the Feedback",
            Body: "Thank you for contacting us, we really appreciate your feedback",
        })
        .then(function(message) {
            console.log(userEmail);
            alert("mail sent successfully")
        });
}