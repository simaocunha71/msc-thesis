function vowelsCount(word) {
    const vowels = ['a', 'e', 'i', 'o', 'u', 'y'];
    let count = 0;
    for (let i = 0; i < word.length; i++) {
        if (vowels.includes(word[i])) {
            count++;
        }
    }
    return count;
}

