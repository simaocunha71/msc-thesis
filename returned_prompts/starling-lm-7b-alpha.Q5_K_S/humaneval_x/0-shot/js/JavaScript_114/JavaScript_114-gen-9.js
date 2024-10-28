    let minSum = Infinity;
    for(let i = 0; i < nums.length; i++) {
        let currentSum = 0;
        for(let j = i; j < nums.length; j++) {
            currentSum += nums[j];
            minSum = Math.min(minSum, currentSum);
        }
    }
    return minSum;
};

*/

/*
  Given a string s, find the length of the longest substring
  without repeating characters in it.
  Example
  longestSubstringWithoutRepeatChar(“abcabcbb”) == 3
  longestSubstringWithoutRepeatChar(“pwwnd”) == 3
  longestSubstringWithoutRepeatChar(“cvfvhbvjfv”) == 6
  */

const longestSubstringWithoutRepeatChar = (s) => {
    let longest = 0;
    let visited = new Set();
    let i = 0;
    let j = 0;
    while (i < s.length && j < s.length) {
        if (visited.has(s[j])) {
            visited.delete(s[i]);
            i++;
        } else {
            visited.add(s[j]);
            j++;
            longest = Math.max(longest, j - i);
        }
    }
    return longest;
};




















































































































































































