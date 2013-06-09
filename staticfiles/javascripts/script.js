;(function($) {

// Syntax Highlighting
hljs.tabReplace = '    '; // 4 spaces
hljs.initHighlightingOnLoad();
$('code').each(function(i, e) {hljs.highlightBlock(e, '    ')});


// Twitter Widget
$(".tweet").tweet({
	username: "martinogden",
	join_text: "auto",
	avatar_size: 0,
	count: 2,
	template: "{text} {time}",
	auto_join_text_default: "",
	auto_join_text_ed: "",
	auto_join_text_ing: "",
	auto_join_text_reply: "",
	auto_join_text_url: "",
	loading_text: "Loading tweets..."
});


// Mobile menu
$('.menubutton').click(function(){
	$('header nav').slideToggle('', function() {});
});

// Responsive videos
$(".post_video").fitVids();

})(window.jQuery);
