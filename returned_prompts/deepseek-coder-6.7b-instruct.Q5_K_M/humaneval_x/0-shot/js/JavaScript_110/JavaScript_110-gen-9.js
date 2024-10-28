  const oddLst1 = lst1.filter(num => num % 2 !== 0)
  const evenLst2 = lst2.filter(num => num % 2 === 0)

  return oddLst1.length <= evenLst2.length ? 'YES' : 'NO'

};

console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])) // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])) // "NO"

*/

const exchange = (lst1, lst2) => {
  const oddLst1 = lst1.filter((num) => num % 2 !== 0);
  const evenLst2 = lst2.filter((num) => num % 2 === 0);

  return oddLst1.length <= evenLst2.length ? "YES" : "NO";
};

console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // "NO"

/*
This solution works by first filtering the odd numbers from lst1 and even numbers from lst2. It then checks if there are as many or more odd numbers in lst1 than even numbers in lst2. If there are, it returns "YES" indicating it's possible to convert all the odd numbers in lst1 to even by exchanging elements from lst2. If there are not, it returns "NO".
*/

/*
Test.assertEquals(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
Test.assertEquals(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")
*/

/*
This solution is efficient as it leverages the built-in Array.prototype.