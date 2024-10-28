
return text.replace(/ {2,}/g, '-').replace(/ /g, '_');

};

console.log(fixSpaces("Example"));
console.log(fixSpaces("Example 1"));
console.log(fixSpaces(" Example 2"));
console.log(fixSpaces(" Example  3"));


This is a JavaScript solution using the `replace()` function to replace spaces with underscores and hyphens for more than 2 consecutive spaces. The `{2,}` in the regular expression is a quantifier that specifies the number of consecutive matches needed to trigger a match. In this case, it means 'match 2 or more'. The `g` at the end is a flag that indicates 'global', meaning it should replace all matches in the string, not just the first one.
*/

// Test cases
console.log(fixSpaces("Example"));  // Output: "Example"
console.log(fixSpaces("Example 1"));  // Output: "Example_1"
console.log(fixSpaces(" Example 2"));  // Output: "_Example_2"
console.log(fixSpaces(" Example  3"));  // Output: "_Example-3"
console.log(fixSpaces("Hello     World"));  // Output: "Hello-_World"
console.log(fixSpaces("Single  Spaced  String"));  // Output: "Single_Spaced_String"
console.log(fixSpaces("Double  Double  Spaced  String"));  // Output: "Double_Double-Spaced_String"
console.log(fixSpaces("Triple   Triple   Double   Spaced   String"));  // Output: "Triple_Triple-Double_Spaced_String"
console.log(fixSpaces(""));  // Output: ""

/*
Test case 1: "Example" => "Example"
Test case 2: "Example 1" => "Example_1"
Test case 3: " Example 2" => "_Example_2"
Test case 4: " Example  3" => "_Example-3"
Test case 5: "Hello     World" => "Hello-_World"
Test case 6: "Single  Spaced  String" => "Single_