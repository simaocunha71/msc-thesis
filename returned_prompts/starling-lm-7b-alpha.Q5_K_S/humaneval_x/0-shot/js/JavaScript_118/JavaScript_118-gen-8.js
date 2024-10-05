    let vowel = ["a", "e", "i", "o", "u"];
    let result = "";
    let left = 0;
    let right = word.length - 1;
    let isVowel = false;

    while (word[left] !== 'a' && word[left] !== 'e' && word[left] !== 'i' && word[left] !== 'o' && word[left] !== 'u' && left < word.length - 1) {
        left++;
    }

    while (word[right] !== 'a' && word[right] !== 'e' && word[right] !== 'i' && word[right] !== 'o' && word[right] !== 'u' && right >= 0) {
        right--;
    }

    if (left < word.length - 1 && right >= 0) {
        for (let i = left + 1; i < word.length - 1; i++) {
            if (vowel.includes(word[i])) {
                result = word[i];
                isVowel = true;
                break;
            }
        }
    }

    if (isVowel) {
        return result;
    } else {
        return "";
    }
};










































































































































































































