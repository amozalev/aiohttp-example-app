try {
    var sock = new WebSocket('ws://' + window.location.host + '/ws');
}
catch (err) {
    var sock = new WebSocket('wss://' + window.location.host + '/ws');
}

// show message
function showMessage(data) {
    var json_obj = $.parseJSON(data);
    var message = json_obj.message;
    var players_num = json_obj.players_num;

    var messageElem = $('#subscribe'),
        height = 0,
        date = new Date();
    options = {hour12: false};
    messageElem.append($('<p>').html('[' + date.toLocaleTimeString('en-US', options) + '] ' + message + '\n'));
    messageElem.find('p').each(function (i, value) {
        height += parseInt($(this).height());
    });

    messageElem.animate({scrollTop: height});
    $('#chat_info').html(players_num);
}

function sendMessage() {
    var msg = $('#message');
    sock.send(msg.val());
    msg.val('').focus();
}

sock.onopen = function () {
    msg = JSON.stringify({"message": 'Connection to server started'})
    showMessage(msg)
};

// send message from form
$('#submit').click(function () {
    sendMessage();
});

$('#message').keyup(function (e) {
    if (e.keyCode == 13) {
        sendMessage();
    }
});

// income message handler
sock.onmessage = function (event) {
    showMessage(event.data);
};

$('#signout').click(function () {
    window.location.href = "signout"
});

sock.onclose = function (event) {
    if (event.wasClean) {
        msg = JSON.stringify({"message": 'Clean connection end'});
        showMessage(msg)
    } else {
        msg = JSON.stringify({"message": 'Connection broken'});
        showMessage(msg)
    }
};

sock.onerror = function (error) {
    showMessage(error);
};