  return [...new Set(l.sort((a, b) => a - b))];
}

console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]));

The function unique takes a list as an argument and returns a new list that contains only the unique elements from the original list. The Set object lets you store unique values of any type. It’s great to use when you need to remove duplicates from an array.

In sort function (a, b) => a - b), we are sorting the array in ascending order.

Finally, we use the spread operator (...) to return the elements of the Set as an array.

*/
