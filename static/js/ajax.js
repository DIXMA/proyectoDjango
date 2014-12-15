$(document).ready(function(){
	$('#search').click(function() {
		var nombre = $('#busqueda').val(); 
  		$.ajax({
  			type: 'GET',
			url: 'lista/',
			data: {'nombre':nombre},			
  			success:function(data){
  				//var obj = jQuery.parseJSON( data );
  				//var ret = "";
  				//$.each(obj, function(i, item) {
    				//ret += (item.fields.nombre)+"<br>";
            $('#historial').html(data);
				} 			
  		});  
  		$.ajax({
  			type: 'GET',
			url: 'tweets/',
			data: {'nombre':nombre},			
  			success:function(data){ 
  				$('#tweets').html(data); 
  			}
  		});		
	}); 

});