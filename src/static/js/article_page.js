hljs.initHighlightingOnLoad();
$(document).ready(function () {
    let pat = /\/p\/(\d+)/;
    let path = window.location.pathname;
    let result = path.match(pat);
    if (result !== null) {
        let postID = result[1];
        $.ajax({
            url: "/articles/" + postID,
            type: "GET",
            success: function (data) {
                if (data.code === 200) {
                    let md = window.markdownit({
                        highlight: function (str, lang) {
                            if (lang && hljs.getLanguage(lang)) {
                                try {
                                    return hljs.highlight(lang, str).value;
                                } catch (__) {
                                }
                            }
                            return ''; // use external default escaping
                        }
                    });
                    let content = md.render(data.data.body);
                    document.title = data.data.title;
                    $(".custom-article-body").empty().append(content);
                }
            }
        })
    }
});