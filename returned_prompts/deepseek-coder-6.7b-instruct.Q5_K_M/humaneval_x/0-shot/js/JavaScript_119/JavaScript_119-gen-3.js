  let str1 = lst[0];
  let str2 = lst[1];
  let count1 = 0;
  let count2 = 0;

  for(let i = 0; i < str1.length; i++){
    if(str1[i] == '(') count1++;
    else if(count1 > 0) count1--;
    else return 'No';
  }

  for(let i = 0; i < str2.length; i++){
    if(str2[i] == ')') count2++;
    else if(count2 > 0) count2--;
    else return 'No';
  }

  if(count1 == count2) return 'Yes';
  else return 'No';
};

console.log(matchParens(['()(', ')'])); // 'Yes'
console.log(matchParens([')', ')'])); // 'No'

The function matchParens checks if it is possible to concatenate the two strings in some order, that the resulting string will be good. It counts the number of '(' and ')' in the first string and checks if the number of '(' is greater than the number of ')'. If it is, it means there is a closing bracket without a corresponding opening bracket, so it returns 'No'. Similarly, it checks the second string. If the number of ')' is greater than the number of '(', it means there is an opening bracket without a corresponding closing bracket, so it returns 'No'. If the counts are equal, it means the string is good, so it returns 'Yes'.

This solution works by keeping track of the number of open and closed parentheses in each string. It iterates through each string, incrementing or decrementing the count as it encounters open or closed parentheses, respectively. If it encounters a closing parenthesis without a corresponding open parenthesis, or a open parenthesis without a corresponding closing parenthesis, it returns 'No'. If the counts are equal at the end of the strings, it returns 'Yes'.
*/

// Solution 2:

function matchParens(lst) {
  let str1 = lst[0];
  let str2