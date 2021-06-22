const urlParams = new URLSearchParams(window.location.search);
const endpoint = urlParams.get('endpoint')
console.log(endpoint)

async function setCount(route) {
    // "http://" + endpoint + "/"
    let resp = await fetch("/api/" + route);
    console.log("http://" + endpoint + "/" + route)
    if (resp.ok) { // if HTTP-status is 200-299
        // get the resp body (the method explained below)
        num = await resp.text();
    } else {
        alert("HTTP-Error: " + resp.status);
    }

    document.getElementById("distance").innerHTML = num + "km";
}

function addCount() {
    setCount("increase");
}

function removeCount() {
    setCount("decrease")
}
