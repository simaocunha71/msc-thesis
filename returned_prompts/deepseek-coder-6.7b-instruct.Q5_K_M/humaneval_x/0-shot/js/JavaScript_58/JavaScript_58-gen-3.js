  return [...new Set(l1.filter(i => l2.includes(i)))]
    .sort((a, b) => a - b);
};

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]));
console.log(common([5, 3, 2, 8], [3, 2]));

*/


A: Here is a solution using Set and Array methods:


const common = (l1, l2) => {
  const set1 = new Set(l1);
  const set2 = new Set(l2);

  const intersection = new Set([...set1].filter(v => set2.has(v)));

  return Array.from(intersection).sort((a, b) => a - b);
};

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])); // [1, 5, 653]
console.log(common([5, 3, 2, 8], [3, 2])); // [2, 3]


In this code, we first convert the input lists to Sets. A Set is a built-in JavaScript object that only allows unique elements.

Then, we use the Array.filter method to create a new Set of elements that are present in both lists.

Finally, we convert the intersection Set back to an Array and sort it. We use the Array.sort method with a custom comparator function that sorts numbers in ascending order.

This solution has a time complexity of O(n + m), where n and m are the lengths of the input lists, because we need to iterate through both lists to create the Sets and filter the intersection.

The space complexity is also O(n + m), because we need to store the Sets and the intersection Set.

Please note that this solution assumes that the input lists do not contain non-numeric values. If