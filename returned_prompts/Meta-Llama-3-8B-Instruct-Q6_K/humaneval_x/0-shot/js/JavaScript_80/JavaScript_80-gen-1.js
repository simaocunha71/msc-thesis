```
function isHappy(s) {
    if (s.length < 3) return false;
    for (let i = 0; i < s.length - 2; i++) {
        const threeConsecutiveLetters = s.slice(i, i + 3);
        if (new Set(threeConsecutiveLetters).size !== 3) return false;
    }
    return true;
}
```


Explanation:
This function checks if the given string 's' is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct. 

First, it checks if the length of the string is less than 3. If it is, it returns false because a happy string must have a length of at least 3.

Then, it iterates over the string with a for loop. For each iteration, it extracts a slice of 3 consecutive letters from the string using the slice() method.

Next, it creates a Set object from the slice of 3 consecutive letters. A Set object is a collection of unique values. 

It then checks if the size of the Set object is equal to 3. If it is, it means that the 3 consecutive letters are distinct, and it returns false.

If the function has not returned false by now, it means that the string is happy, and it returns true. 

This function correctly identifies happy and non-happy strings according to the problem's definition. 





This is a simple and efficient solution that has a time complexity of O(n), where n is the length of the string. It only needs to iterate over the string once and perform a constant amount of work for each character. The space complexity is O(1), which means that the space usage does not grow with the size of the input string.