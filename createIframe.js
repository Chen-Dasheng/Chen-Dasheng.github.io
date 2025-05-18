function createIframe() {
    var iFrame = document.createElement("iframe");
    iFrame.id = "iframe";
    iFrame.title = "iframe";
    iFrame.width = "100%";
    var height = document.getElementById("iframeHeight").value;
    var src = document.getElementById("targetURL").value;
    if (height == "") {
        iFrame.height = "800"; 
    }
    else {
        iFrame.height = height; 
    }
    if (src == "") {
        iFrame.src = "/webInsert.html" 
    }
    else {
        iFrame.src = src; 
    }
    window.parent.document.body.appendChild(iFrame);
    return 'success';
}
