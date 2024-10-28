  let result = "";
  for (let i = word.length - 2; i > 0; i--) {
    if (!/[aeiouAEIOU]/.test(word[i])) {
      if (/[aeiouAEIOU]/.test(word[i + 1])) {
        result = word[i + 1];
        break;
      }
    }
  }
  return result;
}
// You can also use this regular expression to find closest vowel:
// const getClosestVowel = (word) => {
//   let result = "";
//   for (let i = word.length - 2; i > 0; i--) {
//     if (!/[aeiou]/.test(word[i]) && !/[aeiou]/.test(word[i + 1])) {
//       if (/[aeiou]/.test(word[i + 2])) {
//         result = word[i + 2];
//         break;
//       }
//     }
//   }
//   return result;
// }