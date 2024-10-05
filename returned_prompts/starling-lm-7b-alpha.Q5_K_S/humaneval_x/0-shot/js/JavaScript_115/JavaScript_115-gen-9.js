    let row = grid.length, col = grid[0].length;
    let total = 0;

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (grid[i][j] == 1) {
                total += Math.ceil((grid[i][j]) / capacity);
            }
        }
    }
    return total;
};

console.log(maxFill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))
console.log(maxFill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
console.log(maxFill([[0,0,0], [0,0,0]], 5))









*/

*/

/*
Given a string S, find the longest palindromic substring in S. You can assume that the longest palindromic substring has
no more than 1000 characters.

Example 

For inputString "babad", the output should be "bab".
For inputString "cbbd", the output should be "bb".
For inputString "a", the output should be "a".
For inputString "ac", the output should be "a".

Contraints:
1 <= length of S <= 10^5

*/

const longestPalindrome = (inputString) => {

    let res = "";
    let max = 0;
    let i = 0, j = 0;
    while (j < inputString.length) {
        if (j - i > max) {
            res = inputString.slice(i, j + 1);
            max = j - i;
        }
        if (inputString[i] == inputString[j]) {
            i--;
            j++;
        } else {
            if (j - i == 1) {
                i++;
                j++;
            } else