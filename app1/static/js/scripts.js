
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
