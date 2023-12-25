/*You are given a string s.
  Your task is to check if the string is happy or not.
  A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
  For example:
  isHappy(a) => false
  isHappy(aa) => false
  isHappy(abcd) => true
  isHappy(aabb) => false
  isHappy(adb) => true
  isHappy(xyy) => false
  */
const isHappy = (s) => {
  let answer = true;
  for (let i = s.length - 3; i >= 0; i -= 3) {
    let a1 = s[i + 2];
    let a2 = s[i + 1];
    let a3 = s[i];
    if (a1 === a2 && a1 !== "" && a2 !== "" && a1 !== a2) {
      answer = false;
    } else {
      continue;
    }
  }
  return answer;
};
