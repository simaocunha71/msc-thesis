const getClosestVowel = word => {
    let left = word.length - 1;
    let right = 0;
    while (left >= right) {
        if (word[left] === 'a' || word[left] === 'e' || word[left] === 'i' || word[left] === 'o' || word[left] === 'u') {
            return word[left];
        } else if (word[right] === 'a' || word[right] === 'e' || word[right] === 'i' || word[right] === 'o' || word[right] === 'u') {
            return word[right];
        }
        right++;
        left--;
    }
    return '';
}


