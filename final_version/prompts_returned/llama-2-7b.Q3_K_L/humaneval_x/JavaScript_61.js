/* brackets is a string of "(" and ")".
  return true if every opening bracket has a corresponding closing bracket.

  >>> correctBracketing("(")
  false
  >>> correctBracketing("()")
  true
  >>> correctBracketing("(()())")
  true
  >>> correctBracketing(")(()")
  false
  */
const correctBracketing = (brackets) => {
  const length = brackets.length;
  let i, j, idx; // 0-based indexing
  let isCorrect = true; // 2D array of "is this bracket correct" values
  for (i = 1; i < length - 1; i++) {
    const cur = brackets[i];
    if (!cur) continue;
    idx = cur.charCodeAt() - 40; // convert to ascii code of '[' or ']'
    isCorrect[idx][i - 1] = false; // mark as incorrect
  }
  for (j = 2; j < length - 1; j++) {
    const cur = brackets[j];
    if (!cur) continue;
    idx = cur.charCodeAt() - 40; // convert to ascii code of '[' or ']'
    isCorrect[idx][j - 2] = false; // mark as incorrect
  }
  return isCorrect[0][length - 1];
};
