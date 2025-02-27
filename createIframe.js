function CreateIframe(targetURL) {
    var iFrame = document.createElement("iframe");
    iFrame.id = "iframe";
    iFrame.title = "iframe";
    iFrame.width = "100%";
    iFrame.height = "500";
    iFrame.src = targetURL;
    document.body.appendChild(iFrame);
    return 'success';
}
