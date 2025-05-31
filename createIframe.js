function createIframe(targetURL, height) {
    var iframe = document.createElement("iframe");
    iframe.id = "iframe";
    iframe.title = "iframe";
    iframe.width = "100%";
    if (targetURL === undefined) {
        targetURL = "snaplittlebear.top/index.html";
    }
    if (height === undefined) {
       height = "650px"; 
    }
    iframe.frameBorder = "0";
    iframe.src = src; 
    iframe.height = height; 
    iframe.sandbox = "allow-top-navigation allow-same-origin allow-forms allow-scripts";
    if (!targetURL.includes("://")) {
        targetURL = "https://" + targetURL;
    }
    iframe.allowfullscreen = true;
    window.document.body.appendChild(iframe);
    return 'success';
}
