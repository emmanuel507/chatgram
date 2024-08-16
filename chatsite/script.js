// Get the form element
const form = document.getElementById('myForm');

// Add an event listener to the form's submit event
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Redirect to the new HTML file
  window.location.href = 'new_page.html';
});