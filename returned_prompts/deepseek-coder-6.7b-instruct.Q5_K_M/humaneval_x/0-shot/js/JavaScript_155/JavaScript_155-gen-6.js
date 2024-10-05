let count = [0,0]
let nums = Math.abs(num).toString().split('')
nums.forEach(n => n % 2 === 0 ? count[0]++ : count[1]++)
return count
}

console.log(evenOddCount(-12)) // ➞ [1, 1]
console.log(evenOddCount(123)) // ➞ [1, 2]
console.log(evenOddCount(456789)) // ➞ [4, 5]

Explanation:
The function takes an integer as an argument. It first transforms this number into an absolute value (to handle negative numbers) and then transforms this absolute value into a string. This string is then split into an array of its digits. We then use the forEach() method to iterate over this array. For each digit, we check if it is even by using the modulus operation %. If it is even, we increment the first value in the count array by 1. If it is not even (i.e., it is odd), we increment the second value in the count array by 1. Finally, we return the count array.
*/

//Solution 2
function evenOddCount(num) {
    let count = [0, 0];
    let nums = Math.abs(num).toString().split('');
    for(let i = 0; i < nums.length; i++){
        if(nums[i] % 2 === 0){
            count[0]++;
        } else {
            count[1]++;
        }
    }
    return count;
}

console.log(evenOddCount(-12)); // ➞ [1, 1]
console.log(evenOddCount(123)); // ➞ [1, 2]
console.log(evenOddCount(456789)); // ➞ [4, 5]

/*
This solution is similar to the first one, but uses a for loop instead of the forEach method. This makes the code a bit easier to understand.
*/

//Solution 