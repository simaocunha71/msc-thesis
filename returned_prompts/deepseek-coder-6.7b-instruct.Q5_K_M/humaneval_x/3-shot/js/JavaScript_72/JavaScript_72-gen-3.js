  let sum 		= q.reduce((a, b) => a + b, 0);
  let isBalanced 	= q.toString() === q.slice().reverse().toString();

  return sum <= w && isBalanced;
}



