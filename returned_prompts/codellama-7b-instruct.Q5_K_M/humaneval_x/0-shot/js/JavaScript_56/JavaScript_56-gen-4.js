const correctBracketing = (brackets) => {
  return brackets.split('').reduce((a, c) => a + (c === '<' ? 1 : -1), 0) === 0
}

