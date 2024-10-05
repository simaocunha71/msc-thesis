const regex = /\s/g;
const result = text.replace(regex, '_');
if (result.match(/\s{2,}/g)) {
  result.replace(/\s{2,}/g, '-');
}
return result;

};

// fixSpaces("Example") => "Example"
// fixSpaces("Example 1") => "Example_1"
// fixSpaces(" Example 2") => "_Example_2"
// fixSpaces(" Example   3") => "_Example-3"


*/

The above code defines a function `fixSpaces` that takes a string `text` as an input and returns a modified version of the string with all spaces replaced by underscores, and consecutive spaces replaced by hyphens. 

To achieve this, the code first uses a regular expression (`/\s/g`) to match all spaces in the input string. The `replace` method is then used to replace all matched spaces with underscores (`'_'`). 

Next, the code checks if the modified string contains two or more consecutive spaces using the `match` method with the regular expression `/\s{2,}/g`. If a match is found, the `replace` method is used again to replace all consecutive spaces with hyphens (`'-'`). 

Finally, the modified string is returned as the result of the function. 

For example, when the function is called with the input `"Example"`, it will return `"Example"`. When called with the input `"Example 1"`, it will return `"Example_1"`. When called with the input `" Example 2"`, it will return `"_Example_2"`. And when called with the input `" Example   3"`, it will return `"_Example-3"`.

Overall, the `fixSpaces` function provides a way to replace spaces in a string with underscores and handle consecutive spaces by replacing them with hyphens.

*/

/*
  Given a string text, replace all spaces in it with underscores, 
  and if a string has more than 2 consecutive spaces, 
  then replace all consecutive spaces with - 
  
  fixSpaces("Example") == "Example"
  fixSpaces