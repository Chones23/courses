var global_wrapper;
var appgg;
frappe.pages['human-design-for-ind'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Human Design For Individual',
		single_column: true
	});
	global_wrapper=wrapper;
	apgg=new ContentHumanDesign(wrapper);
}
ContentHumanDesign= Class.extend({
	init:function(wrapper){
		var me= this;
		$('<script src="https://embed.bodygraphchart.com/v1/566/js?token=463b83d3-13de-4d69-8132-5507e7f00836" defer></script> <iframe allowfullscreen="" frameborder="0" height="600px" src="https://app.bodygraphchart.com/iframe-test-dimas.html" width="800px"></iframe>').appendTo($(wrapper).find(".layout-main"));
	}
})
