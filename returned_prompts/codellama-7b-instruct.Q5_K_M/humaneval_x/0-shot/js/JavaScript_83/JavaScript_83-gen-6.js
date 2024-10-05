
function startsOneEnds(n) {
    let count = 0;
    for (let i = 1; i <= n; i++) {
        const num = i.toString();
        if (num[0] === "1" || num[num.length - 1] === "1") count++;
    }
    return count;
}
