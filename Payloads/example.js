//This is a example JavaScript payload
//To start create a file named `payloadname.js` and one called `payloadname.js.info`(.info file is not necessary).
//Example of not optimized code.
function logtheconsole(){
console.log( "This is an example" );
alert( "Alert msg" );
}
logtheconsole()
//As you can see the code is very large and clunky, 102 characters to be exact.
//Example of optimized code, with exact same output.
console.log("This is an example");alert("Alert msg");
//This code is 53 characters long. And the way JS functions behave is dependent on what type of xss vulnerability is found.