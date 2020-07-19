$(document).ready(() => {
    let titleList = document.getElementsByClassName("post-title");
    let columnNames = document.getElementsByClassName("column-name");
    let postDates = document.getElementsByClassName("post-date");
    let postSummary = document.getElementsByClassName("post-summary");
    let postLinks = document.getElementsByClassName("post-link");
    $.ajax({
        url: '/articles?per_page=3',
        type: 'GET',
        success: function (data) {
            let result = data.data;
            if (data.code === 200) {
                for (let i = 0; i < titleList.length; i++) {
                    titleList[i].textContent = result[i].title;
                    columnNames[i].textContent = result[i].section;
                    postDates[i].textContent = result[i].create_time;
                    postSummary[i].textContent = result[i].summary;
                    postLinks[i].setAttribute("href", `/p/${result[i].id}`);
                }
            }
        }
    })
});