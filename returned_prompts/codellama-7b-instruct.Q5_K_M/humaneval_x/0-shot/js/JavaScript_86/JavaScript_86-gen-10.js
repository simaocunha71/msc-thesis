const antiShuffle = (str) => {
    const words = str.split(' ');
    const orderedWords = words.map(word => {
        const letters = word.split('');
        letters.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));
        return letters.join('');
    });
    return orderedWords.join(' ');
}

