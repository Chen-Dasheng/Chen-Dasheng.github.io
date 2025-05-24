function createIframe() {
    var height = document.getElementById("iframeHeight").value;
    var src = document.getElementById("targetURL").value;
    if (src == "") {
        var object = document.createElement("object");
        object.id = "object";
        object.title = "object";
        object.width = "100%";
        object.data = "/webInsert.html";
        window.parent.document.body.appendChild(object);
        return'success';
    }
    else {
        var iframe = document.createElement("iframe");
        iframe.id = "iframe";
        iframe.title = "iframe";
        iframe.width = "100%";
        iframe.frameBorder = "0";
        iframe.src = src; 
        if (height == "") {
            iframe.height = "800"; 
        }
        else {
            iframe.height = height; 
        }
        window.parent.document.body.appendChild(iframe);
        return 'success';
    }
}
