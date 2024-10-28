    let max = words[0];
    for (let i = 1; i < words.length; i++) {
        if (max.length < words[i].length) {
            max = words[i];
        } else if (max.length === words[i].length) {
            if (max > words[i]) {
                max = words[i];
            }
        }
    }
    let count = 0;
    let charset = new Set();
    for (let j = 0; j < max.length; j++) {
        if (charset.has(max[j])) {
        } else {
            charset.add(max[j]);
        }
    }
    if (count === charset.size) {
        return max;
    } else {
        return "";
    }
};

findMax(["name", "of", "string"]);
findMax(["name", "enam", "game"]);
findMax(["aaaaaaa", "bb", "cc"]);




function findMax(words) {
    let max = words[0];
    for (let i = 1; i < words.length; i++) {
        if (max.length < words[i].length) {
            max = words[i];
        } else if (max.length === words[i].length) {
            if (max > words[i]) {
                max = words[i];
            }
        }
    }
    let count = 0;
    let charset = new Set();
    for (let j = 0; j < max.length; j++) {
        if (charset.has(max[j])) {
        } else {
            charset.add(max[j]);
        }
    }
    if (count === charset.size) {
        return max;
    } else {
        return "";
    }
};

findMax(["name", "of", "string"]);
findMax(["name", "enam", "game"]);
findMax(["aaaaaaa", "bb", "cc"]);




const findMax =