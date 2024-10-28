const countDistinctCharacters = (string) => {
    let count = 0;
    for (let i = 0; i < string.length; i++) {
        let character = string[i];
        if (character.toLowerCase() !== character.toUpperCase()) {
            count++;
        }
    }
    return count;
};

