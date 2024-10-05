const reverseDelete = (s, c) => {
  let result = [];
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    if (c.indexOf(char) === -1) {
      result.push(char);
    }
  }
  return [result.join(""), result.join("").split("").reverse().join("") === result.join("")];
};

B:
const reverseDelete = (s, c) => {
  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) === -1) {
      result += s[i];
    }
  }
  return [result, result.split("").reverse().join("") === result];
};

C:
const reverseDelete = (s, c) => {
  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) === -1) {
      result += s[i];
    }
  }
  return [result, result.split("").reverse().join("") === result];
};

D:
const reverseDelete = (s, c) => {
  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) === -1) {
      result += s[i];
    }
  }
  return [result, result.split("").reverse().join("") === result];
};

E:
const reverseDelete = (s, c) => {
  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) === -1) {
      result += s[i];
    }
  }
  return [result, result.split("").reverse().join("") === result];
};

F:
const reverseDelete = (s, c) => {
  let result = "";
  for (let i = 0; i < s