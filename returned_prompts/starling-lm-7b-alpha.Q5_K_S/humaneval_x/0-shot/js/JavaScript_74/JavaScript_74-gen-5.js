function totalMatch(lst1, lst2) {
  // Create a variable to store the result
  let result;
  // If both lists are empty, return an empty list
  if (lst1.length === 0 && lst2.length === 0) return [];
  // If the total number of characters in the first list is less than the second, return the first list
  if (lst1.reduce((acc, cur) => acc + cur.length, 0) < lst2.reduce((acc, cur) => acc + cur.length, 0)) {
    result = lst1;
  } else {
    result = lst2;
  }
  // If the total number of characters in the first and second list are equal, return the first list
  if (lst1.reduce((acc, cur) => acc + cur.length, 0) === lst2.reduce((acc, cur) => acc + cur.length, 0)) {
    result = lst1;
  }
  return result;
}

totalMatch([], []); 
totalMatch(['hi', 'admin'], ['hI', 'Hi']); 
totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']); 
totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi']); 
totalMatch(['4'], ['1', '2', '3', '4', '5']);

*/



















































































































































































