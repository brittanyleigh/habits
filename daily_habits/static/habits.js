$(document).ready(function() {

	$('input:checkbox').on('change', function(e){
	  this.form.submit();
	});

	$('#habits-form').submit(function(e){
	    $.post('/', $(this).serialize(), function(data){ });
	    e.preventDefault();
	});
});