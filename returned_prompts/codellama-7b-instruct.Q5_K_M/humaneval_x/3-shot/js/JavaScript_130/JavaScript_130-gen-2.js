  var result = [1, 3];
  if (n == 0) {
    return [1, 3];
  }
  if (n % 2 == 0) {
    result.push((n / 2) + 1);
  } else {
    result.push(tri(n - 1)[result.length] + tri(n - 2)[result.length] + tri(n + 1)[result.length]);
  }
  return result;
}



