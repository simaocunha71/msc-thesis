    let arr = [3];
    if (n === 0) {
        return arr;
    }
    if (n === 1) {
        return arr.concat([1]);
    }
    if (n === 2) {
        return arr.concat([1, 3]);
    }
    for (let i = 3; i <= n; i++) {
        if (i % 2 === 0) {
            arr.push(3);
        } else {
            arr.push(arr[arr.length - 4] + arr[arr.length - 3] + arr[arr.length - 2]);
        }
    }
    return arr;
};


// Keep this function! It helps with testing.
function check(input, expected) {
    if (input !== expected) {
        throw new Error('Expected ' + expected + ' but got ' + input);
    }
}

// Uncomment these tests once you've implemented the function
// check(tri(3), [1, 3, 2, 8]); // true
// check(tri(4), [1, 3, 2, 8, 13]); // true








































































































































































































































