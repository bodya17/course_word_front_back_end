if (localStorage.getItem('x')) {
    document.getElementById('x').value = localStorage.getItem('x');
}

if (localStorage.getItem('y')) {
    document.getElementById('y').value = localStorage.getItem('y');
}

var btn = document.getElementById('submit_btn');
var ua = document.getElementById('ua')
var en = document.getElementById('en')

ua.addEventListener('click', function() {
    localStorage.setItem('x', document.getElementById('x').value)
    localStorage.setItem('y', document.getElementById('y').value)
    window.location = 'http://localhost:5000/ua'
})

en.addEventListener('click', function() {
    localStorage.setItem('x', document.getElementById('x').value)
    localStorage.setItem('y', document.getElementById('y').value)

    window.location = 'http://localhost:5000/en'
})

btn.addEventListener('click', function (e) {

    e.preventDefault();
    var x_vals = document.getElementById('x').value;
    var y_vals = document.getElementById('y').value;

    console.log('fetching')
    fetch('http://localhost:5000/result', {
        method: 'POST',
        body: x_vals + '|' + y_vals
    }).then(function (res) {
        return res.json();
    }).then(function (obj) {
        var trace1 = {
            x: obj.x,
            y: obj.y,
            mode: 'line'
        };

        var trace2 = {
            x: x_vals.split(' '),
            y: y_vals.split(' '),
            mode: 'markers'
        };

        var data = [trace1, trace2];

        var layout = {
            title: 'Line and Scatter Plot',
            height: 400,
            width: 800
        };

        Plotly.newPlot('myDiv', data, layout);

        var formula = document.getElementById('formula');
        formula.innerHTML = `$$ ${obj.formula} $$`;
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, formula]);

    })
})