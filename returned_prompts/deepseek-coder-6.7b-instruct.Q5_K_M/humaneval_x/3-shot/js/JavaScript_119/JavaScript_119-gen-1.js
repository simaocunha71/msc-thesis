  let s1 = lst[0] + lst[1];
  let s2 = lst[1] + lst[0];
  let stack = [];
  for (let s of [s1, s2]) {
    let isGood = true;
    for (let ch of s) {
      if (ch == '(') {
        stack.push(ch);
      } else {
        if (stack.length == 0 || stack[stack.length - 1] != '(') {
          isGood = false;
          break;
        }
        stack.pop();
      }
    }
    if (isGood && stack.length == 0) {
      return "Yes";
    }
    stack = [];
  }
  return "No";
}



