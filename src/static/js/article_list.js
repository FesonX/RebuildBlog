$(document).ready(function () {
    let pat = /\/search\/(\w+)\/(.*)/;
    let blogPat = /\/blog/;
    let path = decodeURI(window.location.pathname);
    let result = path.match(pat);

    let contentTemplate = '<div class="card article-card">\n' +
        '                    <img alt="..." class="card-img-top post-cover" src="...">\n' +
        '                    <div class="card-body">\n' +
        '                        <h5 class="card-title post-title"></h5>\n' +
        '                        <small class="post-author"></small> | <small\n' +
        '                            class="post-date"></small> | <small class="post-pv">10000</small>\n' +
        '                        <p class="card-text post-summary"></p>\n' +
        '                        <a href="#" class="btn btn-outline-info post-link">继续阅读</a>\n' +
        '                    </div>\n' +
        '                </div>';
    let url = '';
    let searchField = '';
    let searchValue = '';
    if (result) {
        searchField = result[1];
        searchValue = result[2];
        url = `/articles/${searchField}/${searchValue}`
    } else if (path.match(blogPat)) {
        url = '/articles'
    }
    $.ajax({
        url: url,
        type: 'GET',
        success: function (data) {
            if (data.code !== 200) {
                return;
            }
            let articles = data.data;
            let articleCount = document.getElementsByClassName("article-total");
            if (articles.length === 0) {
                if (result) {
                    articleCount[0].textContent = `未找到与 "${searchValue}" 相关的文章`;
                } else {
                    articleCount[0].textContent = `未找到相关文章`;
                }
            } else {
                if (result) {
                    articleCount[0].textContent = `找到 ${articles.length} 篇 "${searchValue}" 文章`;
                } else {
                    articleCount[0].textContent = `找到 ${articles.length} 篇文章`;
                }
                let htmlContent = '';
                for (let i = 0; i < articles.length; i++) {
                    htmlContent += contentTemplate;
                }
                $(".article-list-body").empty().html(htmlContent);
                let titleList = document.getElementsByClassName("post-title");
                let postDates = document.getElementsByClassName("post-date");
                let postSummary = document.getElementsByClassName("post-summary");
                let postLinks = document.getElementsByClassName("post-link");
                let postAuthors = document.getElementsByClassName("post-author");
                for (let i = 0; i < titleList.length; i++) {
                    titleList[i].textContent = articles[i].title;
                    postDates[i].textContent = articles[i].create_time;
                    postSummary[i].textContent = articles[i].summary;
                    postLinks[i].setAttribute("href", `/p/${articles[i].id}`);
                    postAuthors[i].textContent = articles[i].username;
                }
            }
        }
    });
});