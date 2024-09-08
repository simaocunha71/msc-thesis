  let openingBracketsCount = 0;
  let closingBracketsCount = 0;

  for (const bracket of brackets) {
    if (bracket == "<") {
      openingBracketsCount += 1;
    } else if (bracket == ">") {
      closingBracketsCount += 1;
    }
  }

  return openingBracketsCount == closingBracketsCount;
}



