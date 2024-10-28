  return [...new Set(l1.filter(i => l2.includes(i)))]
    .sort((a, b) => a - b);
}

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
console.log(common([5, 3, 2, 8], [3, 2]))
module.exports = common;


A: You can use Array.prototype.filter() and Array.prototype.includes() method to achieve this.
Here is the code:


const common = (l1, l2) => {
  return l1.filter(i => l2.includes(i)).sort((a, b) => a - b);
}

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
console.log(common([5, 3, 2, 8], [3, 2]))


This function works by using filter() to create a new array of elements that exist in both l1 and l2 (i.e., are common to both lists). The includes() method is used to determine whether each element of l1 is in l2. The result is then sorted in ascending numerical order using sort().

A: Here is a solution using a Set:


const common = (l1, l2) => {
    let set1 = new Set(l1),
        set2 = new Set(l2),
        intersection = new Set([...set1].filter(x => set2.has(x)));
    return Array.from(intersection).sort((a, b) => a - b);
}

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 12