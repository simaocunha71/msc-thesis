  let reversed = '';
  for (let i = text.length - 1; i >= 0; i--) {
    reversed += text[i];
  }
  return text === reversed;
}
// Alternative solution:
// const isPalindrome = (text) => {
//   return text === text.split('').reverse().join('');
// }
// Alternative solution:
// const isPalindrome = (text) => {
//   let left = 0;
//   let right = text.length - 1;
//   while (left < right) {
//     if (text[left] !== text[right]) {
//       return false;
//     }
//     left++;
//     right--;
//   }
//   return true;
// }