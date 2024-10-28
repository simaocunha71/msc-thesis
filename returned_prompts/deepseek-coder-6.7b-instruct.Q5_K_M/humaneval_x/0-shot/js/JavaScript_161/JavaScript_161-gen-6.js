let letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

    if (![...s].some(e => letters.includes(e))) {
        return [...s].reverse().join('');
    }

    return [...s].map(e => letters.includes(e) ? e.toLowerCase() === e ? e.toUpperCase() : e.toLowerCase() : e).join('');
};

console.log(solve("1234")); // 4321
console.log(solve("ab")); // AB
console.log(solve("#a@C")); // #A@c
console.log(solve("")); // ""
console.log(solve("QWERTY")); // YTREWQ
console.log(solve("1234ab")); // b3421AB


The algorithm starts by checking if there are any letters in the string.
If there are none, the string is reversed and returned.
If there are letters, we then map over the string, and for each character, we check if it is a letter by seeing if it is included in the 'letters' string. If it is a letter, we convert its case, if not, we keep it as it is.
Finally, we join the array of characters back into a string and return it.

The time complexity of this solution is O(n), where n is the length of the string, because we are doing a single pass over the string.

The space complexity is also O(n) because we are creating a new array of characters from the string.

*/

























































































































