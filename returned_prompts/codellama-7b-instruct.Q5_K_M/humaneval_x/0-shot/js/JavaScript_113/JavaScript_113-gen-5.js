const oddCount = (lst) => {
    const result = [];
    for (const str of lst) {
        const num = parseInt(str, 10);
        const odd = num.toString().split('').filter(n => n % 2).length;
        result.push(odd);
    }
    return result;
};

