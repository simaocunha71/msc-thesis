  var depth = 0;
  for (var c of brackets) {
    if (c == '<') {
      depth += 1;
    } else {
      depth -= 1;
    }
    if (depth < 0) {
      return false;
    }
  }
  return depth == 0;
}

Please check my answers. I'm not sure whether I've made any mistakes.