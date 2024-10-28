  if (n == 1) {
    return [1];
  } else if (n % 2 == 0) {
    return [1, n / 2, tri(n - 1)[2], tri(n - 2)[2] + tri(n - 1)[2] + tri(n)[2]];
  } else {
    return [1, tri(n - 1)[1] + tri(n - 2)[1] + tri(n)[1], tri(n - 1)[2] + tri(n - 2)[2] + tri(n)[2]];
  }
}



