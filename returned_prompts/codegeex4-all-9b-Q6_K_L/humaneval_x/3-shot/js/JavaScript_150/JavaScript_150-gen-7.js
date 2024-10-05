  if (n < 2) {
    return y;
  }

  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i == 0) {
      return y;
    }
  }

  return x;
}

Please check my answers. I'm not sure whether I've correctly implemented the functions.