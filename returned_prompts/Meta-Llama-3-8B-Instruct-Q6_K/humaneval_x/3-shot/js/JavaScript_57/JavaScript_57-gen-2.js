  return l.every((x, i) => i == 0 || (x >= l[i - 1]) == (x > l[i - 1]));
} // or: return l.every((x, i) => i == 0 || (x >= l[i - 1]) == (x >= l[0])); (for decreasing)