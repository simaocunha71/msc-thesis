/*Given a list of strings, where each string consists of only digits, return a list.
  Each element i of the output should be "the number of odd elements in the
  string i of the input." where all the i's should be replaced by the number
  of odd digits in the i'th string of the input.

  >>> oddCount(['1234567'])
  ["the number of odd elements 4n the str4ng 4 of the 4nput."]
  >>> oddCount(['3',"11111111"])
  ["the number of odd elements 1n the str1ng 1 of the 1nput.",
   "the number of odd elements 8n the str8ng 8 of the 8nput."]
  */
const oddCount = (lst) => {
  let i;
  const output = [];
  for (i=0; i<lst.length; i++) {
    if (lst[i].match(/\d/)) {
      output.push(`the number of odd elements ${lst[i]} of the input.`);
    } else {
      output.push(`the number of odd elements 2${lst[i]}n of the input.`);
    }
  }
  return output;
};

// EXERCISE ONE:
/*
Given a list of strings, where each string consists of only digits, return a list.
Each element i of the output should be "the number of odd elements in the
string i of the input." where all the i's should be replaced by the number
of odd digits in the i'th string of the input.
>>> oddCount(['1234567'])
["the number of odd elements 4n the str4ng 4 of the 4nput.", "the number of odd elements 3n the str3ng 3 of the 3nput."]
>>> oddCount(['3',"11111111"])
["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput.", "the number of odd elements 