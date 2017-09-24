// $('.loaderImage').hide();

$('#one').click(function() {
	$('.loaderImage').show();
    $.ajax({
		url: '/house1',
		type: 'POST',
		success: function(response){
			// alert('Success: ' + response);
			$('#diagram').attr('src', '/static/img/house1.png');
			$('.loaderImage').hide();
		},
		error: function(error){
			console.log('Error: ' + error);
		}
	});
})
$('#two').click(function() {
	$('.loaderImage').show();
    $.ajax({
		url: '/house2',
		type: 'POST',
		success: function(response){
			// alert('Success: ' + response);
			$('#diagram').attr('src', '/static/img/house2.png');
			$('.loaderImage').hide();
		},
		error: function(error){
			console.log('Error: ' + error);
		}
	});
})
$('#three').click(function() {
	$('.loaderImage').show();
    $.ajax({
		url: '/house3',
		type: 'POST',
		success: function(response){
			// alert('Success: ' + response);
			$('#diagram').attr('src', '/static/img/house3.png');
			$('.loaderImage').hide();
		},
		error: function(error){
			console.log('Error: ' + error);
		}
	});
})