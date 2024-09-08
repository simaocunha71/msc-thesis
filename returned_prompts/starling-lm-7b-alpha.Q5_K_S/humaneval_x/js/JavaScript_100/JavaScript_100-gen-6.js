  const result = [];
  let cur_level = n;
  while (cur_level > 0) {
    if (cur_level % 2 == 0) {
      result.push(cur_level);
      cur_level -= 2;
    } else {
      result.push(cur_level);
      cur_level += 1;
    }
  }
  return result;
}



