Colors = {
    0: '#0FF',
    1: '#F00'
};
currentColor = 0;
maxColors = 2;

rows = 10;
cols = 10;

var onClick = function(div, event)
{
    div.style.backgroundColor = Colors[currentColor];
    currentColor = (currentColor + 1) % maxColors;

    div.onclick = null;

    event.preventDefault();
    return false;
};

function getCell()
{
    var div = document.createElement('div');
    div.className = 'fieldCell';
    div.onclick = onClick.bind(undefined, div);

    return div;
};

function tableCreate() {
    var tbl = document.createElement('table');
    tbl.setAttribute('border', '1');
    var tbdy = document.createElement('tbody');
    for (var i = 0; i < rows; i++)
    {
        var tr = document.createElement('tr');
        for (var j = 0; j < cols; j++) {
			var td = document.createElement('td');
			td.appendChild(getCell());
			tr.appendChild(td)
        }
        tbdy.appendChild(tr);
    }
    tbl.appendChild(tbdy);
    document.body.appendChild(tbl)
}

tableCreate();