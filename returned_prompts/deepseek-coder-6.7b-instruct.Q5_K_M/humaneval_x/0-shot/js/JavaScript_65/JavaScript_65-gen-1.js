let str = String(x);
let len = str.length;

if (shift >= len) {
    return str.split("").reverse().join("");
} else {
    return str.slice(-shift) + str.slice(0, -shift);
}

}

console.log(circularShift(12, 1)) // "21"
console.log(circularShift(12, 2)) // "12"

In this solution, we first convert the input integer x to a string and get its length. Then we check if the shift is greater than or equal to the length of the string. If it is, we reverse the string and return the result. If not, we slice the string into two parts at the position of the shift and return the second part concatenated with the first part.


*/

/*
