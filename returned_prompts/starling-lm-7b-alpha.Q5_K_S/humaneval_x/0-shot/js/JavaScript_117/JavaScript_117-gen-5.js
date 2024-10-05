const consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz";

let result = [];

function helper(i) {
  if (i === s.length) {
    result.push(word);
  } else {
    if (consonants.includes(s[i])) {
      helper(i + 1);
    } else {
      helper(i + 1);
    }
  }
}

let word = "";
for (let i = 0; i < s.length; i++) {
  if (consonants.includes(s[i])) {
    word += s[i];
  } else {
    word += s[i];
  }
  if (word.length === n) {
    helper(i + 1);
    word = "";
  }
}

return result;
};
*/

*/

