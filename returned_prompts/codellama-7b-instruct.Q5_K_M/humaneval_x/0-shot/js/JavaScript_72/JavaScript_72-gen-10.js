const willItFly = (q, w) => {
    if (!q.length || w < q.reduce((a, b) => a + b)) return false;
    for (let i = 0; i < q.length; i++) {
        if (q[i] !== q[q.length - i - 1]) return false;
    }
    return true;
}