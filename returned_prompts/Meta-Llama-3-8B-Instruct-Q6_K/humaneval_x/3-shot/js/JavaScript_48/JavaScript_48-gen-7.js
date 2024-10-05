  let reversed = '';
  for (let i = text.length - 1; i >= 0; i--) {
    reversed += text[i];
  }
  return text === reversed;
} // or
// const isPalindrome = (text) => {
//   return text.split('').reverse().join('') === text;
// } // or
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
// 
// // or
// const isPalindrome = (text) => {
//   text = text.replace(/\s+/g, ''); // remove spaces
//   text = text.toLowerCase(); // to lowercase
//   let reversed = text.split('').reverse().join('');
//   return text === reversed;
// } // or
// const isPalindrome = (text) => {
//   text = text.replace(/\s+/g, ''); // remove spaces
//   text = text.toLowerCase(); // to lowercase
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
// } // or
// const isPalindrome = (text) => {
//   text = text.replace(/\s+/g, ''); // remove spaces
//   text = text.toLowerCase(); // to lowercase
//   return text === text.split('').reverse().join('');
// }
// 
// // or
// const isPalindrome = (text) => {
//   text = text.replace(/\s+/g, ''); // remove spaces
//   text = text.toLowerCase(); // to lowercase
//   let start = 0;
//   let end = text.length - 1;
//   while (start < end) {
//     if (text[start] !== text[end]) {
//       return false;
//     }
//     start++;
//     end--;
//   }
//   return true;
// } // or
// const isPalindrome = (text) => {
//   text = text.replace(/\s+/g, ''); // remove spaces
//  