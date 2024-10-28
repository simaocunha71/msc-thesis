    let vowelCount = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'a' || s[i] === 'e' || s[i] === 'i' || s[i] === 'o' || s[i] === 'u' || s[i] === 'y') {
            vowelCount++;
        }
    }
    return vowelCount;
};

console.log(vowelsCount("abcde"));  // Output: 2
console.log(vowelsCount("ACEDY"));  // Output: 3


// Tests:
console.assert(vowelsCount("abcde") == 2, "Test Case 1 Failed");
console.assert(vowelsCount("ACEDY") == 3, "Test Case 2 Failed");
console.assert(vowelsCount("abcdef") == 3, "Test Case 3 Failed");
console.assert(vowelsCount("ACEDEY") == 3, "Test Case 4 Failed");
console.assert(vowelsCount("ABCDEY") == 1, "Test Case 5 Failed");
console.assert(vowelsCount("ABCDE") == 0, "Test Case 6 Failed");
console.assert(vowelsCount("ABCDEG") == 0, "Test Case 7 Failed");
console.assert(vowelsCount("ABCDEYZ") == 1, "Test Case 8 Failed");
console.assert(vowelsCount("ABCDEFG") == 0, "Test Case 9 Failed");
console.assert(vowelsCount("ABCDEYH") == 1, "Test Case 10 Failed");
console.assert(vowelsCount("ABCDEYI") == 1, "Test Case 11 Failed");
console.assert(vowelsCount("ABCDEYJ") == 1, "Test Case 12 Failed");
console.assert(vowelsCount("ABCDEYK") == 1, "Test Case 13 Failed");
console.