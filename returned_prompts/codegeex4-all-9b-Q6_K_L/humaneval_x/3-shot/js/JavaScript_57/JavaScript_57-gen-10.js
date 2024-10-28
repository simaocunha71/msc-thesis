  var increasing = l.every((a, i) => a <= l[i + 1]);
  var decreasing = l.every((a, i) => a >= l[i + 1]);
  return increasing || decreasing;
}



