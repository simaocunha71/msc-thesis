const correctBracketing = (brackets) => {

  const stack = [];

  for (let i = 0; i < brackets.length; i++) {
    const char = brackets[i];

    if (char === "<") {
      stack.push(char);
    } else if (char === ">") {
      if (stack.pop() !== "<") {
        return false;
      }
    }
  }

  return stack.length === 0;
}

B:
const correctBracketing = (brackets) => {

  let count = 0;

  for (let i = 0; i < brackets.length; i++) {
    const char = brackets[i];

    if (char === "<") {
      count++;
    } else if (char === ">") {
      count--;
    }

    if (count < 0) {
      return false;
    }
  }

  return count === 0;
}

C:
const correctBracketing = (brackets) => {

  let count = 0;

  for (let i = 0; i < brackets.length; i++) {
    const char = brackets[i];

    if (char === "<") {
      count++;
    } else if (char === ">") {
      count--;
    }
  }

  return count === 0;
}
