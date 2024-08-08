// Ensure the DOM is fully loaded before running the script
$(document).ready(function() {
	// Set up a click event listener on the <div> with id="red_header"
	$('#red_header').click(function() {
	    // Change the color of the <header> element to red (#FF0000)
	    $('header').css('color', '#FF0000');
	});
});

