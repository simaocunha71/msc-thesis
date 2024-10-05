
const isNested = string => {
  let stack = [];
  for (let bracket of string) {
    if (bracket == "[" || bracket == "(") stack.push(bracket);
    else if (bracket == "]" || bracket == ")") {
      if (stack.length == 0) return false;
      let last = stack.pop();
      if (last == "[" && bracket == "]") return false;
      if (last == "(" && bracket == ")") return false;
    }
  }
  return stack.length == 0;
};

B:
const isNested = (string) => {
  let stack = [];
  for (let bracket of string) {
    if (bracket == "[" || bracket == "(") stack.push(bracket);
    else if (bracket == "]" || bracket == ")") {
      if (stack.length == 0) return false;
      let last = stack.pop();
      if (last == "[" && bracket == "]") return false;
      if (last == "(" && bracket == ")") return false;
    }
  }
  return stack.length == 0;
};

C:
const isNested = (string) => {
  let stack = [];
  for (let bracket of string) {
    if (bracket == "[" || bracket == "(") stack.push(bracket);
    else if (bracket == "]" || bracket == ")") {
      if (stack.length == 0) return false;
      let last = stack.pop();
      if (last == "[" && bracket == "]") return false;
      if (last == "(" && bracket == ")") return false;
    }
  }
  return stack.length == 0;
};
