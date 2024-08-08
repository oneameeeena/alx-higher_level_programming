// Ensure the DOM is fully loaded before running the script
$(document).ready(function() {
	// Set up a click event listener on the <div> with id="red_header"
	$('#red_header').click(function() {
		// Add the class 'red' to the <header> element
		$('header').addClass('red');
	});
});
