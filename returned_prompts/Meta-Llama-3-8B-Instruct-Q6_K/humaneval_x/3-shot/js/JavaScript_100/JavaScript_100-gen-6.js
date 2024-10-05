  let pile = [];
  let numStones = n;
  while (numStones > 0) {
    pile.push(numStones);
    if (numStones % 2 === 0) {
      numStones += 1;
    } else {
      numStones += 2;
    }
  }
  return pile.reverse();
}
// The function `makeAPile` takes an integer `n` as input and returns a list of integers representing the number of stones in each level of the pile. The function works by initializing an empty list `pile` and a variable `numStones` to the input `n`. It then enters a loop that continues until `numStones` is 0. In each iteration of the loop, it pushes `numStones` to the `pile` list and then updates `numStones` to be the next odd or even number depending on whether `numStones` is odd or even. Finally, it returns the `pile` list in reverse order to get the correct order of levels.