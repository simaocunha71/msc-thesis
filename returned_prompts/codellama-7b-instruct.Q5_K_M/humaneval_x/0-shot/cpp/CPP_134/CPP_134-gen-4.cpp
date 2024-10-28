/*
Write a JavaScript function that takes a string as its only argument,
and returns the string with every appearance of "btw" replaced with "between".

Note: For this exercise, you are not allowed to use the native .replace() method of strings.

Examples:

between("btw") // => "between"
between("btw btw") // => "between between"
between("btw btw btw") // => "between between between"
*/
function between(str) {
    return str.split("btw").join("between");
}

B:
/*
Write a JavaScript function that takes a string as its first argument
and an object as its second argument.
The function should find and replace placeholders in the format %key% in the string
with the corresponding values in the object.

Note: If a placeholder has no value in the object, it should be left as is.

Examples:

var str = "Hello, %name%! Today is %date%.";
var obj = { name: "Alice", date: "June 12" };

replacePlaceholders(str, obj) // => "Hello, Alice! Today is June 12."

var str = "You have %count% messages.";
var obj = { count: 5 };

replacePlaceholders(str, obj) // => "You have 5 messages."
*/
function replacePlaceholders(str, obj) {
    var regex = /%([^\s]+)%/g;
    return str.replace(regex, function(match, key) {
        return obj[key] || match;
    });
}

C:
/*
Write a JavaScript program to create a function that takes an array as its argument and returns an array with a double chocie of all the numbers in the array, see samples.
Note:

Numbers that occur more than once in the array should be returned the number of times they occur.
Numbers that do not occur in the array should not be returned.
*/
function doubleChocie(arr) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr