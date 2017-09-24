$('#one').click(function() {
    $.ajax({
		url: '/house1',
		type: 'POST',
		success: function(response){
			alert('Success: ' + response);
			$('#diagram').attr('src', '/static/img/house1.png');
		},
		error: function(error){
			console.log('Error: ' + error);
		}
	});
})
$('#two').click(function() {
    $.ajax({
		url: '/house2',
		type: 'POST',
		success: function(response){
			alert('Success: ' + response);
			$('#diagram').attr('src', '/static/img/house2.png');
		},
		error: function(error){
			console.log('Error: ' + error);
		}
	});
})
$('#three').click(function() {
    $.ajax({
		url: '/house3',
		type: 'POST',
		success: function(response){
			alert('Success: ' + response);
			$('#diagram').attr('src', '/static/img/house3.png');
		},
		error: function(error){
			console.log('Error: ' + error);
		}
	});
})