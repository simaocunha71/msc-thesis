  return ((x+y===z) || (x+z===y) || (y+z===x)) && (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z));
}

console.log(anyInt(5, 2, 7)); // ➞ true
console.log(anyInt(3, 2, 2)); // ➞ false
console.log(anyInt(3, -2, 1)); // ➞ true
console.log(anyInt(3.6, -2.2, 2)); // ➞ false

// The function first checks if the sum of any two numbers equals the third one.
// Then it checks if all three numbers are integers.
```

</div>



</div>



</div>



<div class="tasks_item">

## Task 3
<div class="content">
<div class="question">
