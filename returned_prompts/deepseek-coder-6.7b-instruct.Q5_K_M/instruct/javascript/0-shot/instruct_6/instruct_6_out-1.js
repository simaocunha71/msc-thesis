
    Here's an example of how the function should work:

    uniqueTokens('hello world', 'world hello') 
    // returns: ""

    uniqueTokens('hello world goodbye', 'world hello') 
    // returns: "goodbye"

    uniqueTokens('hello world', '') 
    // returns: "hello world"

    uniqueTokens('hello hello world', 'hello') 
    // returns: "world"
*/

function uniqueTokens(s1, s2) {
    let arr1 = s1.split(" ");
    let arr2 = s2.split(" ");
    let result = [];
    for(let i=0; i<arr1.length; i++){
        let isUnique = true;
        for(let j=0; j<arr2.length; j++){
            if(arr1[i] === arr2[j]){
                isUnique = false;
                break;
            }
        }
        if(isUnique){
            result.push(arr1[i]);
        }
    }
    return result.join(" ");
}

console.log(uniqueTokens('hello world', 'world hello')); // returns: ""
console.log(uniqueTokens('hello world goodbye', 'world hello')); // returns: "goodbye"
console.log(uniqueTokens('hello world', '')); // returns: "hello world"
console.log(uniqueTokens('hello hello world', 'hello')); // returns: "world"

/*
    This function works by first splitting the input strings into arrays of tokens.
    Then it iterates over the first array, checking each token against the second array.
    If it finds a match, it breaks out of the inner loop and continues to the next token in the first array.
    If it doesn't find a match, it adds the token to the result array.
    Finally, it joins the result array into a string and returns it.
*/














































