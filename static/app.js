function callApi(ID) {
    document.getElementById("resultDiv").innerHTML = "";

    var request = new XMLHttpRequest();

    if(ID) {
        var id_num = document.getElementById("id").value;
        request.open('GET', 'http://127.0.0.1:8000/athletes/?id=' + id_num, true);
    } else {
        request.open('GET', 'http://127.0.0.1:8000/athletes/', true);
    }

    // Send request
    request.send();

    request.onload = function () {


        if (request.status == 200) {

        // Begin accessing JSON data here
        var data = JSON.parse(this.response);

            var table = "<table><tr>" +
                        "<th>First Name</th>" +
                        "<th>Last Name</th>" +
                        "<th>Weight</th>" +
                        "<th>Height</th></tr>";

            for (var result in data) {
                for (var id in data[result]) {
    //              Add table rows
                    table += "<tr>" +
                            "<td>" + data[result][id]["firstName"] + "</td>" +
                            "<td>" + data[result][id]["lastName"] + "</td>" +
                            "<td>" + data[result][id]["weight"] + "</td>" +
                            "<td>" + data[result][id]["height"] + "</td>" +
                            "</tr>";
                }
             }

             table += "</table>";

             document.getElementById("resultDiv").innerHTML = table;
        } else if (request.status == 400 || request.status == 404) {
            document.getElementById("resultDiv").innerHTML = "Error - Bad Request";
            console.log('Error - Bad Request');
        }
    }
}

