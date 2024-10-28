let triSequence = [3];

if (n === 0) {
    return [3];
} else if (n === 1) {
    triSequence.push(1);
    return triSequence;
} else if (n === 2) {
    triSequence.push(2);
    return triSequence;
} else {
    triSequence.push(2);
    triSequence.push(8);
}

for (let i = 3; i <= n; i++) {
    if (i % 2 === 0) {
        triSequence.push(1 + i / 2);
    } else {
        triSequence.push(triSequence[i - 1] + triSequence[i - 2] + triSequence[i]);
    }
}

return triSequence;
}

console.log(tri(3)); 
console.log(tri(4));
console.log(tri(5));
console.log(tri(6));

This code should output the first n + 1 numbers of the Tribonacci sequence.

It's a little bit complicated because we have to handle the special cases (n=0, n=1, n=2) first, 
and the sequence is calculated as per the given rules.

The tribonacci sequence starts with 3, 1, 2, 8, 14, 26, 48, 88, 154, 272, 486, 860, 1478, 2560, 4382, 7416, 12508, 21154, 35848, 60614, 101440, 168278, 277208, 454326, 741672, 1207014, 1961352, 3185414, 5201520, 8432342, 13553928, 21622470, 342763