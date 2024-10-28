const antiShuffle = (s) => {
    let words = s.split(" ");
    let result = "";
    for (let i = 0; i < words.length; i++) {
        let word = words[i];
        let sorted = word.split("").sort();
        result += sorted.join("");
        if (i < words.length - 1) {
            result += " ";
        }
    }
    return result;
};