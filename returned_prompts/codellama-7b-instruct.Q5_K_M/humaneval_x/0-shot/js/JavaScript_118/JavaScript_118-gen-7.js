const getClosestVowel = (word) => {
let vowels = ["a", "e", "i", "o", "u"];
let lastVowel = "";
let firstVowel = "";
let lastConsonant = "";
let firstConsonant = "";
word = word.toLowerCase();
let wordLength = word.length;
for (let i = 0; i < wordLength; i++) {
    if (vowels.includes(word[i])) {
        lastVowel = word[i];
    }
    if (vowels.includes(word[wordLength - 1 - i])) {
        firstVowel = word[wordLength - 1 - i];
    }
    if (word[i].match(/[A-Z]/i)) {
        lastConsonant = word[i];
    }
    if (word[wordLength - 1 - i].match(/[A-Z]/i)) {
        firstConsonant = word[wordLength - 1 - i];
    }
}
if (lastConsonant && firstConsonant && lastVowel && firstVowel) {
    return lastVowel;
} else {
    return "";
}
}

