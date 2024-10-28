Here is the solution to the problem:

```javascript
const totalMatch = (lst1, lst2) => {
  const total1 = lst1.reduce((acc, cur) => acc + cur.length, 0);
  const total2 = lst2.reduce((acc, cur) => acc + cur.length, 0);
  
  if (total1 < total2) return lst1;
  if (total1 > total2) return lst2;
  
  return lst1;
};
```


This function uses the reduce() method to calculate the total number of characters in each list. It then compares these totals and returns the list with the smaller total. If the totals are equal, it returns the first list. The reduce() method takes a callback function as its first argument, which is called for each element in the list. The callback function takes two arguments: the accumulator (acc) and the current element (cur). The accumulator is used to store the sum of the lengths of the strings in the list, and the current element is the length of the current string. The callback function returns the sum of the accumulator and the current element, which is then used as the new accumulator for the next iteration. The reduce() method returns the final value of the accumulator, which is the total number of characters in the list. The totalMatch() function then compares these totals and returns the appropriate list.