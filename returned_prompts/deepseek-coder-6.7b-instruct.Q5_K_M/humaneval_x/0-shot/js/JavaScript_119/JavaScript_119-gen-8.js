  let str1 = lst[0];
  let str2 = lst[1];
  let count1 = 0, count2 = 0;
  
  for(let i = 0; i < str1.length; i++){
    if(str1[i] == '(') count1++;
    if(str1[i] == ')') count1--;
    if(count1 < 0) return 'No';
  }
  if(count1 != 0) return 'No';
  
  for(let i = 0; i < str2.length; i++){
    if(str2[i] == '(') count2++;
    if(str2[i] == ')') count2--;
    if(count2 < 0) return 'No';
  }
  if(count2 != 0) return 'No';
  
  return 'Yes';
};

// Test cases:
console.log(matchParens(['()(', ')'])); // 'Yes'
console.log(matchParens([')', ')'])); // 'No'


The logic of the solution is quite straightforward. We iterate through both strings and increment/decrement a counter based on whether we encounter an opening or closing parenthesis. If at any point the counter becomes negative, or if it doesn't end at zero, we return 'No'. If it passes all these conditions, we return 'Yes'.

This solution has a time complexity of O(n) and a space complexity of O(1), where n is the total length of both strings.

Note: This solution assumes that the input will always be valid (two strings with only parentheses). If this is not the case, you may want to add some error checking to handle invalid inputs.
  
*/
