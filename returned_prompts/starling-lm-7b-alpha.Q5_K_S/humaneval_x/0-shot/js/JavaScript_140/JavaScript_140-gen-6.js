let text = text.split("");
let result = [];

for (let i = 0; i < text.length; i++) {
  if (text[i] === " ") {
    if (i > 0 && i < text.length - 1 && text[i - 1] === " " && text[i + 1] === " ") {
      result.push("-");
      text[i + 1] = "";
    } else {
      result.push("_");
    }
  } else {
    result.push(text[i]);
  }
}

return result.join("");

};













*/
//O(n)
function fixSpaces(text) {
  let result = "";
  let count = 0;
  let last = "";
  for (let i = 0; i < text.length; i++) {
    if (text[i] === " ") {
      count++;
      if (count === 2) {
        result += "-";
        count = 0;
      }
    } else {
      result += "_";
      count = 0;
    }
  }
  return result + "_";
}


*/
























































































































































































































