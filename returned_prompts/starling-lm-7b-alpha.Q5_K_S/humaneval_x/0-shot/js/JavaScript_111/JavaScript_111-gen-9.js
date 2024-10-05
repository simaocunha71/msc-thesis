
let letters = test.split(' ');
let letterCount = {};
let maxCount = 0;

for(let i = 0; i < letters.length; i++) {
    if(letterCount[letters[i]] === undefined) {
        letterCount[letters[i]] = 1;
    } else {
        letterCount[letters[i]]++;
    }
}

for(let prop in letterCount) {
    if(letterCount[prop] > maxCount) {
        maxCount = letterCount[prop];
    }
}

let result = {};

for(let prop in letterCount) {
    if(letterCount[prop] === maxCount) {
        result[prop] = maxCount;
    }
}

return result;

};

/*
 * Parameters
 * test: string
 *
 * Returns
 * {
 *      letter: count
 * }
 *
 * Example:
 * histogram('a b c'); // { 'a': 1, 'b': 1, 'c': 1 }
 * histogram('a b b a'); // { 'a': 2, 'b': 2 }
 * histogram('a b c a b'); // { 'a': 2, 'b': 2 }
 * histogram('b b b b a'); // { 'b': 4 }
 * histogram(''); // {}
 */


*/

Answer:

let letters = test.split(' ');
let letterCount = {};
let maxCount = 0;

for(let i = 0; i < letters.length; i++) {
    if(letterCount[letters[i]] === undefined) {
        letterCount[letters[i]] = 1;
    } else {
        letterCount[letters[i]]++;
    }
}

for(let prop in letterCount) {
    if(letterCount[prop] > maxCount) {
        maxCount = letterCount[prop];
    }
}

let result = {};

for(let prop in letterCount) {
    if(letterCount[prop] === maxCount) {
        result[prop] = max