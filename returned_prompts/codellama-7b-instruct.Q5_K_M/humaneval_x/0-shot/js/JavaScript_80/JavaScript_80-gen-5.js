const isHappy = (s) => {
    const len = s.length;
    if (len < 3) return false;
    let a = 0;
    let b = 0;
    let c = 0;
    for (let i = 0; i < len; i++) {
        if (s[i] === s[i + 1] && s[i + 1] === s[i + 2]) {
            a++;
            b++;
            c++;
        }
    }
    return a < 2 && b < 2 && c < 2;
};
