$(function() {
  /*
   * Syntax Highlighting
   */
  hljs.tabReplace = '    '; // 4 spaces
  hljs.initHighlightingOnLoad();
  $('code').each(function(i, e) {hljs.highlightBlock(e, '    ')});
});
