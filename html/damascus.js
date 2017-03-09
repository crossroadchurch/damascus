channel_exclusive = [false, false, false, false]

function pollServer(){
    $.getJSON(
        "/poll",
        function(data, status){
            if (!channel_exclusive[0]) { $("#c001").slider("value", data.c001); }
            if (!channel_exclusive[1]) { $("#c002").slider("value", data.c002); }
            if (!channel_exclusive[2]) { $("#c003").slider("value", data.c003); }
            if (!channel_exclusive[3]) { $("#c004").slider("value", data.c004); }
        }
    )
};

$( function() {
    $("#c001").slider({
        orientation: "vertical",
        range: "min",
        min: 0,
        max: 255,
        value: 0,
        slide: function(event, ui) {
            $.getJSON("/channel/1/" + ui.value);
        },
        start: function(event, ui) {
            channel_exclusive[0] = true;
        },
        stop: function(event, ui) {
            channel_exclusive[0] = false;
        }
    });
    $("#c002").slider({
        orientation: "vertical",
        range: "min",
        min: 0,
        max: 255,
        value: 0,
        slide: function(event, ui) {
            $.getJSON("/channel/2/" + ui.value);
        },
        start: function(event, ui) {
            channel_exclusive[1] = true;
        },
        stop: function(event, ui) {
            channel_exclusive[1] = false;
        }
    });
    $("#c003").slider({
        orientation: "vertical",
        range: "min",
        min: 0,
        max: 255,
        value: 0,
        slide: function(event, ui) {
            $.getJSON("/channel/3/" + ui.value);
        },
        start: function(event, ui) {
            channel_exclusive[2] = true;
        },
        stop: function(event, ui) {
            channel_exclusive[2] = false;
        }
    });
    $("#c004").slider({
        orientation: "vertical",
        range: "min",
        min: 0,
        max: 255,
        value: 0,
        slide: function(event, ui) {
            $.getJSON("/channel/4/" + ui.value);
        },
        start: function(event, ui) {
            channel_exclusive[3] = true;
        },
        stop: function(event, ui) {
            channel_exclusive[3] = false;
        }
    });
});

$.ajaxSetup({ cache: false });
setInterval("pollServer()", 500);
