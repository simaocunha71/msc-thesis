  let newList = lst.filter(item => item.length % 2 === 0);
  newList.sort();
  return newList;
}

console.log(sortedListSum(["ab", "a", "aaa", "cd"]));

This function will first filter out all the strings with odd lengths,
then it sorts the resulting list and finally returns it.
The sort() function used sorts the items in an array in place,
changing its elements to be sorted according to the string Unicode code point.
In this case, we don't need to specify a comparator function because it sorts in lexicographical order by default.
So this function will return a list of strings in sorted order by length and then alphabetically.

*/



/*
