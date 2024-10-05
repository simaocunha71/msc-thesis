if (s.length < 3) return false;
for (let i = 0; i < s.length - 2; i++) {
    if (s[i] === s[i + 1] || s[i] === s[i + 2] || s[i + 1] === s[i + 2]) {
        return false;
    }
}
return true;
}

console.log(isHappy("a")); // false
console.log(isHappy("aa")); // false
console.log(isHappy("abcd")); // true
console.log(isHappy("aabb")); // false
console.log(isHappy("adb")); // true
console.log(isHappy("xyy")); // false

```

**Explanation:**

In the solution, we first check if the length of the string is less than 3. If it is, we return false since there won't be enough letters for 3 consecutive letters to be distinct.

Then, we iterate over the string using a loop that runs until the third last letter. For each letter, we check if it is the same as the next letter or the letter after that. If either of these conditions is true, we return false since the letters aren't distinct. If we've gone through the loop without returning false, we return true since all letters are distinct.

The time complexity of this solution is O(n), where n is the length of the string. This is because we're iterating over the string once. The space complexity is O(1), as we're using a constant amount of space to store the input string.

I hope this helps clear up the question. If you have any more questions, feel free to ask.



























































































































