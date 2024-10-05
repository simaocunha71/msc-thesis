
    let arr = []
    for(let i = 1; i <= n; i++)
    {
        arr.push(i*i - i + 1);
    }
    let count = 0;
    for(let i = 0; i < arr.length; i++)
    {
        for(let j = i + 1; j < arr.length; j++)
        {
            for(let k = j + 1; k < arr.length; k++)
            {
                if((arr[i] + arr[j] + arr[k])%3 == 0)
                    count++;
            }
        }
    }
    return count;
}

*/

/*
  You are given a string s of lowercase English letters, and an array of strings words. You want to build a string of words from the given words such that the characters in the string have the same order as in the string s.

  Return the number of ways to construct such a string.
  Two strings are equal if they have the same length and the same characters, regardless of the order of the characters. For example, "abc" and "acb" are considered the same string.

  If there are multiple valid ways to build the string, they are considered the same. For example, "abc" and "acb" are considered the same.
  It can be proven that the number of ways to construct a valid string is the same regardless of the order of the characters. Therefore, you don't need to consider the order of the characters in the array words.


Example 1:

  Input: s = "cat", words = ["c","a","t","act"]
  Output: 2
  Explanation: The two ways to construct the string are "cat" and "act".


Example 2:

  Input: s = "cab", words = ["c","ab","cab"]
  Output: 1
  Explanation: The only way to construct the string is "cab".


Example 3:

  Input: s = "abcd", words = ["abcd","cdab","adcb","cbda"]
  Output: 4
  Explanation: One way