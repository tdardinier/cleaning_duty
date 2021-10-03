// Make table cells clickable and add checkboxes
(function() {
    const tbody = document.getElementsByTagName("tbody")[0];
    for (var i = 0, row; row = tbody.rows[i]; i++) {
        for (var j = 1, col; col = row.cells[j]; j++) {
            col.setAttribute("onclick", "check(" + i + ", " + (j + j % 2) + "); leaderboard();");
            col.setAttribute("style", "cursor: pointer; user-select: none")
        }
    }
})();

// Toggle checkbox
function check(i, j) {
    const checkbox = document.getElementsByTagName("tbody")[0].rows[i].cells[j].getElementsByTagName("input")[0];
    checkbox.checked = !checkbox.checked;
}

// Load data into JavaScript object array
function load() {
    var abody = [];
    const headings = document.getElementsByTagName("thead")[0].getElementsByTagName('th');
    const tbody = document.getElementsByTagName("tbody")[0];
    for (var i = 0, row; row = tbody.rows[i]; i++) {
        var duties = [];
        for (var j = 1, col; col = row.cells[j]; j += 2) {
            var checked = row.cells[j + 1].getElementsByTagName("input")[0].checked;
            duties.push({person: col.innerText.trim(), job: headings[j].innerText, checked: checked});
        }
        var week = row.cells[0].innerText.split(" - ");
        abody.push({week_start: week[0], week_end: week[1], duties: duties});
    }
    return abody;
}

// Display leaderboard
function leaderboard() {
    const abody = load();
    var person_stats = []
    abody.forEach(function(week) {
        week.duties.forEach(function(duty) {
            if (duty.person in person_stats === false) {
                person_stats[duty.person] = {checked: 0, unchecked: 0};
            }
            duty.checked ? person_stats[duty.person].checked++ : person_stats[duty.person].unchecked++;
            person_stats[duty.person].completed = person_stats[duty.person].checked / (person_stats[duty.person].checked + person_stats[duty.person].unchecked);
        });
    });

    var leaderboard = '<table style="margin-top:10px"><tbody>';
    for (const [key, value] of Object.entries(person_stats)) {
        leaderboard += "<td>" + key + " "+ (Math.round(value.completed * 10000) / 100) + "%" + "</td>";
    }
    leaderboard += "</tbody></table>";
    document.getElementById("leaderboard").innerHTML = leaderboard;
}
