
return text.replace(/ {2,}/g, '-').replace(/ /g, '_');

};

console.log(fixSpaces("Example"));
console.log(fixSpaces("Example 1"));
console.log(fixSpaces(" Example 2"));
console.log(fixSpaces(" Example  3"));


*/

The function fixSpaces uses two replace functions to accomplish the task.

The first replace function / {2,}/g is used to replace all occurrences of two or more consecutive spaces with a single dash (-). This uses a regular expression pattern that matches two or more consecutive spaces.

The second replace function / /g is used to replace all single spaces with an underscore (_). This uses a regular expression pattern that matches a single space.

The results of these two replacements are combined with the '+' operator to create the final result.

In the end, the function returns the modified string.
*/


// Answer: 

function fixSpaces(text) {
  return text.replace(/ {2,}/g, '-').replace(/ /g, '_');
}

console.log(fixSpaces("Example")); // "Example"
console.log(fixSpaces("Example 1")); // "Example_1"
console.log(fixSpaces(" Example 2")); // "_Example_2"
console.log(fixSpaces(" Example  3")); // "_Example-3"

// Explanation:

// In the first replace function, / {2,}/g is used to match 2 or more spaces. In the second replace function, / /g is used to match 1 space. 

// In both cases, replace function is used to replace the matched spaces with the required character.

// The final output is the modified string.




































































































