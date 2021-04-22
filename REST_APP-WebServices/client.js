var hprose = require("hprose");
var client = hprose.Client.create("http://127.0.0.1:8181/");
var proxy = client.useService();
proxy.ping(function(result) {
    console.log(result);
});
