  let oddLst1 = lst1.filter(x => x % 2 !== 0);
  let evenLst2 = lst2.filter(x => x % 2 === 0);

  return oddLst1.length <= evenLst2.length ? "YES" : "NO";
}

console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])) // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])) // "NO"

//Explanation:
//In the first case, we can exchange 1 from lst1 and 1 from lst2 to make lst1 consist only of even numbers.
//In the second case, there are no even numbers in lst2 to exchange with odd numbers in lst1, so we can't make lst1 consist only of even numbers.

In the first case, we can exchange 1 from lst1 and 1 from lst2 to make lst1 consist only of even numbers.
In the second case, there are no even numbers in lst2 to exchange with odd numbers in lst1, so we can't make lst1 consist only of even numbers.

The function works by first filtering the odd numbers in lst1 and the even numbers in lst2. It then compares the lengths of these filtered arrays. If the length of oddLst1 is less than or equal to the length of evenLst2, then it returns "YES", because we can exchange the elements of lst1 and lst2 to make lst1 consist only of even numbers. Otherwise, it returns "NO".

The function assumes that the input lists will be non-empty and that the numbers are integers.
*/

























































































