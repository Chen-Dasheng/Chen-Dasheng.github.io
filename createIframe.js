function createIframe() {
    var iFrame = document.createElement("iframe");
    iFrame.id = "iframe";
    iFrame.title = "iframe";
    iFrame.width = "100%";
    iFrame.height = document.getElementById("iframeHeight").value;
    iFrame.src = document.getElementById("targetURL").value;
    document.body.appendChild(iFrame);
    return 'success';
}
