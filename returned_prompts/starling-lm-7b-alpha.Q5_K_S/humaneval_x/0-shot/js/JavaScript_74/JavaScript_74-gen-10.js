function totalMatch(lst1, lst2) {
    // Create a variable to store the result
    let result = [];

    // Calculate the total length of the strings in the first list
    let total1 = lst1.reduce((acc, curr) => acc + curr.length, 0);

    // Calculate the total length of the strings in the second list
    let total2 = lst2.reduce((acc, curr) => acc + curr.length, 0);

    // Compare the total length of the strings in the two lists
    if (total1 < total2) {
        result = lst1;
    } else if (total1 === total2) {
        result = lst1;
    } else {
        result = lst2;
    }

    // Return the result
    return result;
}

console.log(totalMatch([], [])); 
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])); 
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])); 
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])); 
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5']));

*/

*/

function totalMatch(lst1, lst2) {
    // Create a variable to store the result
    let result = [];

    // Calculate the total length of the strings in the first list
    let total1 = lst1.reduce((acc, curr) => acc + curr.length, 0);

    // Calculate the total length of the strings in the second list
    let total2 = lst2.reduce((acc, curr) => acc + curr.length, 0);

    // Compare the total length of the strings in the two lists
    if (total1 < total2) {
        result = lst1;
    } else if (total1 === total2) {
        result = lst1;
    } else {
        result = lst2;
    }

    // Return the result
   