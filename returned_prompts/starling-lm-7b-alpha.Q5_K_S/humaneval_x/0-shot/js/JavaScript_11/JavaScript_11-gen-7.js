    let result = '';

    for (let i = 0; i < a.length; i++) {
        result += (a[i] === b[i]) ? 0 : 1;
    }

    return result;
};

console.log(stringXor('010', '110'));


// Given two binary strings, perform binary XOR on these inputs and return result also as a string.

Explanation:
To solve this problem, we need to understand how to perform XOR operation on binary strings. In a XOR operation, if the bits at the corresponding positions in the two input strings are the same (either both 0 or both 1), the result at that position is 0. If the bits are different (one is 0 and the other is 1), the result is 1.

In the provided solution, a function called `stringXor` is defined that takes two binary strings `a` and `b` as input. It initializes an empty string called `result` to store the XOR result.

The function then uses a `for` loop to iterate over each character in the input strings. For each character, it compares the corresponding characters in `a` and `b`. If they are the same, it appends 0 to the `result` string; otherwise, it appends 1.

Finally, the function returns the `result` string, which represents the XOR of the input strings.

In the provided example, the function is called with the arguments `'010'` and `'110'`. The XOR operation is performed on these strings, resulting in the string `'100'`. This value is then printed to the console using `console.log`.

Overall, this solution effectively solves the problem of performing binary XOR on two input strings and returns the result as a string.

*/


// Given two binary strings, perform binary XOR on these inputs and return result also as a string.

Explanation:
To solve this problem, we need to understand how to perform XOR operation on binary strings. In a XOR operation, if the bits at the corresponding positions in the two input strings are the same (either both 0 or both 1), the result at that position