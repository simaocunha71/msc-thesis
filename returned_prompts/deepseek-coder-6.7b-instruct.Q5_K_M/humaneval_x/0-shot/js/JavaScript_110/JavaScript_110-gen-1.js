  const oddLst1 = lst1.filter(num => num % 2 !== 0);
  const evenLst2 = lst2.filter(num => num % 2 === 0);

  return oddLst1.length <= evenLst2.length ? 'YES' : 'NO';
}

/*
Test.assertEquals(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
Test.assertEquals(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")
*/

This solution works by first filtering out the odd numbers in lst1 and even numbers in lst2. It then checks if the number of odd numbers in lst1 is less than or equal to the number of even numbers in lst2. If it is, then it is possible to exchange elements between lst1 and lst2 to make all elements in lst1 even, so the function returns "YES". Otherwise, it returns "NO".

*/

// Solution 2

const exchange = (lst1, lst2) => {
  const oddLst1 = lst1.filter(n => n % 2 !== 0);
  const evenLst2 = lst2.filter(n => n % 2 === 0);

  return oddLst1.length <= evenLst2.length ? 'YES' : 'NO';
}

// Solution 3

const exchange = (lst1, lst2) => {
  const oddLst1 = lst1.filter(n => n % 2 !== 0);
  const evenLst2 = lst2.filter(n => n % 2 === 0);

  return oddLst1.length <= evenLst2.length ? 'YES' : 'NO';
}

// Solution 4

const exchange = (lst1, lst2) => {
  const oddLst1 = lst1.filter(n => n % 2 !== 0);
  const evenLst2 = lst2.filter(n