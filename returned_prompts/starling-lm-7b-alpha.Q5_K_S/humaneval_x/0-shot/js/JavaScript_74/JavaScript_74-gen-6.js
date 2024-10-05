
totalMatch(['4'], ['1', '2', '3', '4', '5'])

Here's one way to solve the problem:

function totalMatch(lst1, lst2) {
  let total1 = lst1.reduce((acc, curr) => acc + curr.length, 0);
  let total2 = lst2.reduce((acc, curr) => acc + curr.length, 0);
  if (total1 < total2) {
    return lst1;
  } else if (total1 > total2) {
    return lst2;
  } else {
    return lst1;
  }
}

Explanation:
This solution uses the reduce() method to calculate the total length of all strings in each list. It compares these totals and returns the corresponding list.

The reduce() method is used to add up the lengths of each string in the list. The initial value of the accumulator (acc) is set to 0, and for each string (curr) in the list, the length of the string is added to the accumulator. The result is stored in total1 and total2.

The if-else statements then compare total1 and total2 to determine which list is shorter. If total1 is less than total2, lst1 is returned. If total1 is greater than total2, lst2 is returned. If the totals are equal, the first list (lst1) is returned, as specified in the problem statement.

For example, in the given test case totalMatch(['4'], ['1', '2', '3', '4', '5']), the total length of the strings in the first list is 1 (the length of '4'), and the total length of the strings in the second list is 10 (the sum of the lengths of all five strings). Since the total length of the first list is less than the total length of the second list, the first list is returned.

This solution has a time complexity of O(n), where n is the total number of strings in both lists.

Alternatively, you can use the spread operator and the sort() method to compare the lengths of each string directly, without using reduce(). Here's an example of how to do this:

function totalMatch(lst