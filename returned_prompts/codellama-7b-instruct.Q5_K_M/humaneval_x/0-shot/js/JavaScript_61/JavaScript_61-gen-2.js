const correctBracketing = (brackets) => {
  let stack = [];
  for (let i = 0; i < brackets.length; i++) {
    const bracket = brackets[i];
    if (bracket === "(") {
      stack.push(bracket);
    } else if (bracket === ")") {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length === 0;
};


//   let count = 0;
//   for (let i = 0; i < brackets.length; i++) {
//     if (brackets[i] === '(') {
//       count++;
//     } else if (brackets[i] === ')') {
//       count--;
//     }
//     if (count < 0) {
//       return false;
//     }
//   }
//   return count === 0;

// }


// function correctBracketing(brackets) {
//   if (brackets === "(") {
//     return false;
//   }
//   const arr = brackets.split('');
//   const stack = [];
//   for (let i = 0; i < arr.length; i++) {
//     const bracket = arr[i];
//     if (bracket === '(') {
//       stack.push(bracket);
//     } else if (bracket === ')') {
//       if (stack.length === 0) {
//         return false;
//       } else {
//         stack.pop();
//       }
//     }
//   }
//   return stack.length === 0;
// }
