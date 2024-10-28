  let result = [];
  for(let i = 0; i < game.length; i++) {
    result.push(Math.abs(game[i] - guess[i] ));
  }
  return result;
}

console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]));
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]));

*/
</code>
</pre>
</div>
</body>
</html>
<html>
<body>
<h2>JavaScript Codewars Challenges</h2>
<h3>Challenge 1: Create a function that takes two numbers as arguments and returns their sum</h3>
<p>Here is the JavaScript code for the challenge:</p>

<div>
<pre>
<code>
function add(a, b){
  return a + b;
}

console.log(add(10, 2)); // Output: 12
</code>
</pre>
</div>

<p>This function takes two parameters, a and b. It returns the sum of these two numbers. The console.log() function is used to test the function.</p>
</body>
</html>


<html>
<body>
<h2>JavaScript Codewars Challenges</h2>
<h3>Challenge 2: Create a function