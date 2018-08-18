$(document).ready(function() {

	$('#habits-form').submit(function(e){
	    $.post('/', $(this).serialize(), function(data){ });
	    e.preventDefault();
	});
	
	$('input:checkbox').on('change', function(e){
	  this.form.submit();
	});

	$('.checkbox input:checkbox').on('click', function(){
		$(this).siblings('label').addClass('checked');
	});
});