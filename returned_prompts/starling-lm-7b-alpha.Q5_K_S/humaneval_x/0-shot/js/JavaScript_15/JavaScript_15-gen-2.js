    let result = "";
    for (let i = 0; i <= n; i++) {
        result += i + " ";
    }
    return result;
};

console.log(stringSequence(0));
console.log(stringSequence(5));

/*
    The above code is a simple implementation of the problem statement.
    We initialize an empty string `result` and a loop to iterate from 0 to n.
    Inside the loop, we concatenate the current number i and a space character to the result.
    Finally, we return the result after the loop is over.

    Time complexity: O(n)
    Space complexity: O(1)
*/

