  let maxDepth = [];
  let currentDepth = 0;
  let currentGroup = [];
  let currentChar = "";
  for (const c of paren_string) {
    if (c == ' ' || c == ')') {
      if (currentDepth > maxDepth[maxDepth.length - 1]) {
        maxDepth.push(currentDepth);
      } else if (currentDepth < maxDepth[maxDepth.length - 1]) {
        maxDepth.pop();
      }
      currentDepth = 0;
      currentGroup = [];
    } else if (c == '(') {
      currentDepth += 1;
      currentGroup.push(c);
    } else if (c == ')') {
      currentDepth -= 1;
      currentGroup.push(c);
    }
    // console.log(c + ": " + currentDepth + " - " + currentGroup);
  }
  if (currentDepth > maxDepth[maxDepth.length - 1]) {
    maxDepth.push(currentDepth);
  } else if (currentDepth < maxDepth[maxDepth.length - 1]) {
    maxDepth.pop();
  }
  return maxDepth;
}



