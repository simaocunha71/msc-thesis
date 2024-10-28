  const oddLst1 = lst1.filter(n => n % 2 !== 0);
  const evenLst2 = lst2.filter(n => n % 2 === 0);

  return oddLst1.length <= evenLst2.length ? "YES" : "NO";
}

console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])) // => "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])) // => "NO"


The function works by first filtering the odd numbers from lst1 and even numbers from lst2. Then it checks if the count of the odd numbers in lst1 is less or equal to the count of even numbers in lst2. If it is true, it means that we can exchange elements between lst1 and lst2 to make all the numbers in lst1 even, so it returns "YES", otherwise it returns "NO".

I hope this helps 😉.

If you have any more questions, feel free to ask.


*/

// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
// --
//