  const length = string.length;

  for (var i = 2; i <= Math.sqrt(length); i++) {
    if (length % i == 0) {
      return false;
    }
  }

  return true;
}



