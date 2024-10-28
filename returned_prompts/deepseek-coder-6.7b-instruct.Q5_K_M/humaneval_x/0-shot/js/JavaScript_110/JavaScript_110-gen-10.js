  let oddLst1 = lst1.filter(x => x % 2 !== 0);
  let evenLst2 = lst2.filter(x => x % 2 === 0);

  return oddLst1.length <= evenLst2.length ? "YES" : "NO";
}

console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // "NO"

In this solution, we first filter out the odd numbers from lst1 and even numbers from lst2.
Then we compare the lengths of the filtered odd numbers list and the filtered even numbers list.
If the length of the odd numbers list in lst1 is less than or equal to the length of the even numbers list in lst2, we return "YES", meaning we can make all the numbers in lst1 to be even by exchanging. Otherwise, we return "NO".

*/

const exchange = (lst1, lst2) => {
  let oddLst1 = lst1.filter((x) => x % 2 !== 0);
  let evenLst2 = lst2.filter((x) => x % 2 === 0);

  return oddLst1.length <= evenLst2.length ? "YES" : "NO";
};

console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // "NO"

/*
This solution works by filtering the odd numbers from the first list and even numbers from the second list.
If the number of odd numbers in the first list is less than or equal to the number of even numbers in the second list, the function returns "YES", indicating that it is possible to make the first list of even numbers by exchanging elements from the second list. If not, it returns "