const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

let left = 0;
let right = word.length - 1;

while (left < right) {
  const mid = Math.floor((left + right) / 2);
  const char = word[mid];

  if (vowels.includes(char)) {
    right = mid;
  } else {
    left = mid + 1;
  }
}

return left > right ? '' : word[right];
};

getClosestVowel("yogurt");


*/

In this question, we are given a word and we need to find the closest vowel that stands between two consonants from the right side of the word (case sensitive). We are also given a list of vowels and we need to check if the character in the word is a vowel. If it's a vowel, we need to update the right pointer to the position of the vowel. If it's not a vowel, we need to update the left pointer to the next position. We continue this process until the left pointer is greater than the right pointer. If the left pointer is greater than the right pointer, it means that there are no vowels between the consonants, so we return an empty string. If the left pointer is less than the right pointer, it means that there is a vowel between the consonants, so we return the character at the right pointer.

For example, if we are given the word "yogurt", the first character is 'y' and it's a consonant, so we update the left pointer to the next position. The second character is 'o' and it's a vowel, so we update the right pointer to the position of the vowel. The third character is 'g' and it's a consonant, so we update the left pointer to the next position. The fourth character is 'u' and it's a vowel, so we update the right pointer to the position of the vowel. The fifth character is 'r' and it's a consonant, so we update the left pointer