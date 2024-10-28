    const arr1 = arr.filter(x => x >= 1 && x <= 9);
    arr1.sort((a, b) => a - b);
    const arr2 = arr1.reverse();
    const arr3 = arr2.map(x => {
        if (x === 1) { return "One"; }
        if (x === 2) { return "Two"; }
        if (x === 3) { return "Three"; }
        if (x === 4) { return "Four"; }
        if (x === 5) { return "Five"; }
        if (x === 6) { return "Six"; }
        if (x === 7) { return "Seven"; }
        if (x === 8) { return "Eight"; }
        if (x === 9) { return "Nine"; }
    });
    return arr3;
};

const byLength2 = (arr) => {
    let arr1 = arr.filter(x => x >= 1 && x <= 9);
    arr1.sort((a, b) => a - b);
    let arr2 = arr1.reverse();
    return arr2.map(x => {
        if (x === 1) { return "One"; }
        if (x === 2) { return "Two"; }
        if (x === 3) { return "Three"; }
        if (x === 4) { return "Four"; }
        if (x === 5) { return "Five"; }
        if (x === 6) { return "Six"; }
        if (x === 7) { return "Seven"; }
        if (x === 8) { return "Eight"; }
        if (x === 9) { return "Nine"; }
    });
};

module.exports = { byLength, byLength2 };

*/


