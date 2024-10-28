let openParenCount = 0;
let closeParenCount = 0;
let parenGroups = [];
let currentGroup = "";

for (let i = 0; i < paren_string.length; i++) {
    let char = paren_string[i];
    if (char === '(') {
        openParenCount++;
    }
    if (char === ')') {
        closeParenCount++;
    }
    if (openParenCount === closeParenCount) {
        parenGroups.push(currentGroup);
        currentGroup = "";
        openParenCount = 0;
        closeParenCount = 0;
    } else {
        currentGroup += char;
    }
}
return parenGroups;
};





// In the above program, the function separateParenGroups takes in a string of characters called paren_string.
// The function counts the number of open and closed parentheses in the string, and uses these counts to determine
// when a balanced set of parentheses is encountered.

// The function then appends each set of balanced parentheses to the parenGroups array,
// and resets the counts of open and closed parentheses for the next set.

// This process continues until all sets of balanced parentheses have been identified and added to the parenGroups array.

// Finally, the function returns the parenGroups array, which contains all of the sets of balanced parentheses found in the original string.

// This function is useful in situations where one needs to identify and separate sets of balanced parentheses from a larger string of characters.







































































































































