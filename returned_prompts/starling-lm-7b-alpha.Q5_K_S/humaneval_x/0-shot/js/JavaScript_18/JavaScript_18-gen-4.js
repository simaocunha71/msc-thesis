    let count = 0;
    for (let i = 0; i < string.length; i++) {
        let j = i;
        while (j < string.length && string[j] === substring[0]) {
            j++;
        }
        if (j - i >= substring.length) {
            count++;
        }
        i = j - 1;
    }
    return count;
};

console.log(howManyTimes("aaa", "aa"));
console.log(howManyTimes("aaaa", "aa"));
console.log(howManyTimes("aaaxaaaxaaayayaaayaxayaxayayayayaxayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayay