const selectWords = (s, n) => {
    let res = [];
    let i = 0;
    let j = 0;
    while (i < s.length) {
        if (s[i] !== ' ') {
            j++;
            if (j === n) {
                res.push(s.substring(i - n, i));
                j = 0;
            }
        } else {
            j = 0;
        }
        i++;
    }
    return res;
};


