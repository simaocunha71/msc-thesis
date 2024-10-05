function totalMatch(lst1, lst2) {
  // if both lists are empty, return an empty list
  if (lst1.length === 0 && lst2.length === 0) {
    return [];
  }
  // if the first list is empty, return the second list
  if (lst1.length === 0) {
    return lst2;
  }
  // if the second list is empty, return the first list
  if (lst2.length === 0) {
    return lst1;
  }

  // calculate the total number of characters in each list
  const total1 = lst1.reduce((acc, curr) => acc + curr.length, 0);
  const total2 = lst2.reduce((acc, curr) => acc + curr.length, 0);

  // if the total number of characters in the first list is less than the total number of characters in the second list, return the first list
  if (total1 < total2) {
    return lst1;
  }
  // if the total number of characters in the first list is greater than the total number of characters in the second list, return the second list
  if (total1 > total2) {
    return lst2;
  }
  // if the total number of characters in both lists is the same, return the first list
  return lst1;
}

totalMatch(["4"], ["1", "2", "3", "4", "5"]); // ["4"]

*/

/*
  Write a function that takes in an array of strings and returns an array of the same length containing the length of each string.

  Examples
  lengthArr(["cat", "dog"]) ➞ [3, 3]
  lengthArr(["elephant", "hippo", "gorilla"]) ➞ [9, 5, 7]
  lengthArr([]) ➞ []
  lengthArr(["Hello", "World"]) ➞ [5, 5]
  lengthArr(["Hello", "World", "!"]) ➞ [5, 5, 1]

  Notes:
  - The input will always