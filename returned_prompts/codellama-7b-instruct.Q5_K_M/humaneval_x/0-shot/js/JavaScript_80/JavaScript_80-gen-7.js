const isHappy = (s) => {
    if (s.length < 3) return false;
    let arr = [];
    for (let i = 0; i < s.length; i++) {
        if (arr.includes(s[i]) && arr[i + 1] === s[i + 1] && arr[i + 2] === s[i + 2]) return false;
        else arr.push(s[i]);
    }
    return true;
}
