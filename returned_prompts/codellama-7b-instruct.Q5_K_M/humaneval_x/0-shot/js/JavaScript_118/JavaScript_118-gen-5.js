const getClosestVowel = word => {
const vowels = ['a', 'e', 'i', 'o', 'u'];
let closestVowel = '';
for (let i = word.length - 1; i >= 0; i--) {
const char = word[i];
if (char === ' ') continue;
if (vowels.includes(char)) {
closestVowel = char;
break;
}
}
return closestVowel;
}

