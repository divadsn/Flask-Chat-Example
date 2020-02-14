var socket;
            
$(document).ready(function(){
    socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');

    $('#text').keypress(function(e) {
        var code = e.keyCode || e.which;
        if (code == 13) {
            // wysyłanie wiadomości
        }
    });
});

function leave_room() {
    // wyjście z czatu
}