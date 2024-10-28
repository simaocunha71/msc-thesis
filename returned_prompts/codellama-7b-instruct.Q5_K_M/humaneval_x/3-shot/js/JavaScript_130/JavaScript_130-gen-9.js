  if (n == 0) {
    return [1];
  } else if (n % 2 == 0) {
    return [1, tri(n - 1)[0] + tri(n - 2)[0] + tri(n + 1)[0]];
  } else {
    return [1, tri(n - 1)[0] + tri(n - 2)[0] + tri(n + 1)[0], tri(n - 1)[0] + tri(n - 2)[0] + tri(n - 1)[0]]
  }
}



