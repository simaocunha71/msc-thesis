    let max = '';
    let maxCount = 0;

    for (const word of words) {
        let count = 0;
        for (const c of word) {
            if (word.indexOf(c) === word.lastIndexOf(c)) {
                count++;
            }
        }
        if (count > maxCount) {
            max = word;
            maxCount = count;
        } else if (count === maxCount && word < max) {
            max = word;
        }
    }
    return max;
};

findMax(["name", "of", "string"]); // "string"
findMax(["name", "enam", "game"]); // "enam"
findMax(["aaaaaaa", "bb", "cc"]); // "aaaaaaa"


// Optimized

function findMax(words) {
    let max = '';
    let maxCount = 0;
    for (const word of words) {
        const unique = new Set(word).size;
        if (unique > maxCount) {
            max = word;
            maxCount = unique;
        } else if (unique === maxCount && word < max) {
            max = word;
        }
    }
    return max;
}



// Optimized

function findMax(words) {
    let max = '';
    let maxCount = 0;
    for (const word of words) {
        const unique = new Set(word).size;
        if (unique > maxCount) {
            max = word;
            maxCount = unique;
        } else if (unique === maxCount && word < max) {
            max = word;
        }
    }
    return max;
}

findMax(["name", "of", "string"]); // "string"
findMax(["name", "enam", "game"]); // "enam"
findMax(["aaaaaaa", "bb", "cc"]); // "aaaaaaa"



// Optimized

function findMax(words) {
    let max = '';
    let maxCount = 0;
    for (const word