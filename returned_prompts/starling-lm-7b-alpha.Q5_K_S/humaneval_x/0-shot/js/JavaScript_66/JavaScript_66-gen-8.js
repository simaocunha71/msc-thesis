  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (c === c.toUpperCase()) {
      sum += c.charCodeAt(0);
    }
  }
  return sum;
};

console.log(
  digitSum(""), // 0
  digitSum("abAB"), // 131
  digitSum("abcCd"), // 67
  digitSum("helloE"), // 69
  digitSum("woArBld"), // 131
  digitSum("aAaaaXa") // 153
);





// Here are some additional tests you might run to verify that your function works.
// These tests are not exhaustive and you don't need to include them in your solution.

console.log(
  digitSum("AaAb"), // 102
  digitSum("12345"), // 18
  digitSum("abcdefghijklmnopqrstuvwxyz"), // 0
  digitSum("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), // 2202
  digitSum("abcDEFGHIJKLMNOPQRSTUVWXYZ"), // 235
  digitSum("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), // 3001
  digitSum("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), // 6003
  digitSum("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), // 9006
  digitSum("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY