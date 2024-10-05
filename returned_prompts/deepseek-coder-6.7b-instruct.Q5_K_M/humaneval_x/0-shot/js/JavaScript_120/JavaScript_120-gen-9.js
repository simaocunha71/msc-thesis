  arr.sort((a, b) => b - a);

  return arr.slice(0, k);
};

console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1));
console.log(maximum([4, -4, 4], 2));
console.log(maximum([-3, -4, 5], 3));


/*
  The function maximum sorts the array in descending order and then returns the 
  first k elements of the sorted array. This gives the maximum k elements in the array.

  The time complexity of this solution is O(n log n), where n is the size of the array. 
  This is because we are sorting the array. The space complexity is O(1), because we are 
  not using any additional space that scales with the input size.
 */
</code>

</section>

<section class="slide">

<h2>Python Code</h2>

<code style="font-size: 20px;">
