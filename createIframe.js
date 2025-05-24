function createIframe(targetURL, height) {
    var height = height || document.getElementById("iframeHeight").value;
    var src = targetURL || document.getElementById("targetURL").value;
    if (src == "") {
        var object = document.createElement("object");
        object.width = "100%";
        object.data = "/webInsert.html";
        window.document.body.appendChild(object);
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
        window.document.body.appendChild(iframe);
        return 'success';
    }
}
