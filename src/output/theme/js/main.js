$('document').ready(function (){
	$('#share-box').sharrre({
	  share: {
	    googlePlus: true,
	    facebook: true,
	    twitter: true
	  },
	  buttons: {
	    googlePlus: {size: 'tall'},
	    facebook: {layout: 'box_count'},
	    twitter: {count: 'vertical', via: 'khan_io'}
	  },
	  hover: function(api, options){
	    $(api.element).find('.buttons').show();
	  },
	  hide: function(api, options){
	    $(api.element).find('.buttons').hide();
	  },
	  enableTracking: true
	});
});