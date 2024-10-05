  var max = null;

  for (const s of strings) {
    if (max == null || s.length > max.length) {
      max = s;
    }
  }

  return max;
}



