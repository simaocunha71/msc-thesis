  let res = [];
  
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] === x) {
        res.push([i, j]);
      }
    }
  }
  
  return res.sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });
}

console.log(getRow([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1)) // [ [ 0, 0 ], [ 1, 4 ], [ 1, 0 ], [ 2, 5 ], [ 2, 0 ] ]
console.log(getRow([], 1)) // []
console.log(getRow([[], [1], [1, 2, 3]], 3)) // [ [ 2, 2 ] ]

//Time complexity of this solution is O(n*m) where n is the number of rows and m is the number of columns in the list.
//Space complexity of this solution is also O(n*m) in the worst case scenario when all elements in the list are equal to x.
</code></pre>
</div>

</body>
</html>
<html>
<body>
<div id="main">
<h2>JavaScript: Find the number of occurrences of a specific letter in a string</h2>
<pre><code>
