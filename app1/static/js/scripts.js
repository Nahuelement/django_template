
document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', function() {
      var navbar = document.querySelector('.navbar');
      if (window.scrollY > 50) {
        navbar.classList.add('navbar-color');
      } else {
        navbar.classList.remove('navbar-color');
      }
    });
  });

//   var bottonNavbar = document.querySelector(".navbar-toggler");


//   bottonNavbar.addEventListener("click", function() {
//     var navbar = document.querySelector('.navbar');
//     // Aquí puedes colocar el código de la función que deseas ejecutar
//     // alert("¡El botón ha sido presionado!");
//     navbar.classList.add('navbar-color');
//     // Otras instrucciones...
//   });