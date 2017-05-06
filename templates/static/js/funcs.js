var template = '<div class="p">'+'<h2></h2>'+'<p></p>'+'</div>';

var api_product = "http://127.0.0.1:8000/MySales/products/api/"
var api_order = "http://127.0.0.1:8000/MySales/orders/api/"
var api_user = "http://127.0.0.1:8000/MySales/accounts/api/"


function addProduct(){
	var $div = $(template);
	var dom = $(this).parent('#new-product');
	var name = dom.find('#product-name').val();
	var description = dom.find('#product-description').val();

	$.ajax({
		'url': api_product,
		'type': 'POST',
		'data': {name: name, description: description},
		'dataType': 'json'
	}).done(function(response){
		// console.log("post success");
		// console.log(response);
		
		dom.find('#product-name').val("");
		dom.find('#product-description').val("");
		$div.find('h2').text(response.name);
		$div.find('p').text(response.description);
		$div.append('<button class="ajax-delete" id="'+response.id+'">Delete</button>')
		$div.appendTo('#product-list');

	}).fail(function(e){
		console.log(e);
	});

	
}

function deleteProduct(){
		var id = $(this).attr('id');
		var dom = $(this).parent('.p');
		// console.log(api+id);
		$.ajax({
			'url': api_product+id,
			'type': 'DELETE'
		}).done(function(){
			console.log("delete success");
			dom.remove();
		}).fail(function(e){
			console.log(e);
		});
}

function addOrder(request){
	console.log("add order");
	var user = $(this).attr('user');
	var product = $(this).parent('.p').attr('product');
	$.ajax({
		'url': api_order,
		'type': 'POST',
		'data': {user: user, product: product},
		'dataType': 'json'
	}).done(function(){
		console.log("add success");
	}).fail(function(e){
		console.log(e);
	});
}

function deleteOrder(request){
	console.log("delete order");
	var dom = $(this).parent('.o');
	var id = dom.attr('order');
	$.ajax({
		'url': api_order+id,
		'type': 'DELETE'
	}).done(function(){
		console.log("delete success");
		dom.remove();
	}).fail(function(e){
		console.log(e);
	});

}

function deleteCustomer(request){
	console.log("delete customer");	
	var dom = $(this).parent('.c');
	var id = dom.attr('customer');
	$.ajax({
		'url': api_user+id,
		'type': 'DELETE'
	}).done(function(){
		console.log("delete customer success");
		dom.remove();
	}).fail(function(e){
		console.log(e);
	});
}


(function ($){

	$(document).on('click', '#create-product', addProduct);
	$(document).on('click', '.ajax-delete', deleteProduct);
	$(document).on('click', '.add-order', addOrder);
	$(document).on('click', '.delete-order', deleteOrder);
	$(document).on('click', '.delete-customer', deleteCustomer);



})(jQuery);


