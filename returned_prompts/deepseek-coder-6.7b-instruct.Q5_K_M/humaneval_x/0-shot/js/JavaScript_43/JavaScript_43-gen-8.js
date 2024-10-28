  let set = new Set();
  for(let i of l) {
    if(set.has(-i)) {
      return true;
    }
    set.add(i);
  }
  return false;
};

console.log(pairsSumToZero([1, 3, 5, 0]));
console.log(pairsSumToZero([1, 3, -2, 1]));
console.log(pairsSumToZero([1, 2, 3, 7]));
console.log(pairsSumToZero([2, 4, -5, 3, 5, 7]));
console.log(pairsSumToZero([1]));

```

##### Solution Explanation:
This solution makes use of a `Set` in JavaScript which is an object that lets you store unique values. We initialize a `Set` and iterate over the input list `l`. For each element `i` in `l`, we check if the `Set` already contains `-i`. If it does, we return `true` because we found two distinct elements that sum to zero. If we get through the entire list without finding such elements, we return `false`.

This solution runs in O(n) time, where n is the length of the input list, because we make one pass over the list. It also uses O(n) space to store the `Set`.

The key to this problem is understanding that if you have two numbers that sum to zero, then you can represent one of them as the negative of the other. By using a `Set`, we can store the numbers we have seen so far and check if we have seen the number that would make the sum zero.

This solution assumes that the input list will only contain integers. If the input list can contain non-integer elements, we would need to modify the solution to handle that case.

Please note that the question asked for distinct elements, so we return `true` as soon as we find a pair summing to zero, without checking the rest of the list.

The question asked for a solution in JavaScript, but the question and solution provided here can be adapted to any other language.

```

##### Solution Explanation:
This solution