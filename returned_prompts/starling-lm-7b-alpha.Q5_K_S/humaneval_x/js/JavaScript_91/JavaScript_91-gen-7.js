  let result = 0;
  let idx = 0;
  while (idx < S.length) {
    let next_idx = S.indexOf("I", idx);
    if (next_idx >= 0) {
      let sentence_end = S.indexOf('.', next_idx);
      sentence_end = Math.max(S.indexOf('?', next_idx), S.indexOf('!', next_idx));
      result += 1;
      idx = sentence_end + 1;
    } else {
      idx = S.length + 1;
    }
  }
  return result;
}



