  let openingBracketsCount = 0;
  let closingBracketsCount = 0;

  for (const c of brackets) {
    if (c == "(") {
      openingBracketsCount += 1;
    } else if (c == ")") {
      closingBracketsCount += 1;
    }
  }

  return openingBracketsCount == closingBracketsCount;
}



