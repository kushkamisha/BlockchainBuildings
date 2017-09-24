$('#one').click(function() {
    $('#diagram').attr('src', '/static/img/1.png');
    $.ajax({
		url: '/run',
		type: 'POST',
		success: function(response){
			alert('Success: ' + response);
		},
		error: function(error){
			console.log('Error: ' + error);
		}
	});
})
$('#two').click(function() {
    $('#diagram').attr('src', '/static/img/2.png');
})
$('#three').click(function() {
    $('#diagram').attr('src', '/static/img/3.png');
})