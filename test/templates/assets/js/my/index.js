var spiderList = document.querySelector('.spider-list');
getData();

function getData() {
    $.ajax({
        url: "http://localhost:9090/SpiderList" + "?t=" + ( new Date() ).getTime().toString(),
        success: function(res) {
            // console.log(JSON.stringify(result));
            showData(res.data);
        },
        error: function(err) {
            console.log(JSON.stringify(err));
        }
    });
}

function showData(data) {
    var tmp = '';
    for(var i=0; i<data.length; i++) {
        tmp += '<tr class="odd gradeX">';
        tmp += '<th>' + data[i].id + '</th>';
        tmp += '<th>' + data[i].spiderName + '</th>';
        tmp += '<th>' + data[i].url + '</th>';
        tmp += '<th>' + data[i].isAgent + '</th>';
        tmp += '<th>' + data[i].startTime + '</th>';
        tmp += '<th>' + data[i].isStart + '</th>';
        tmp += '<th>操作图标待定</th>';
        tmp += '</tr>'
    }
    spiderList.insertAdjacentHTML('beforeend', tmp);
}
