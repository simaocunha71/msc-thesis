  const length = string.length;
  let prime = false;

  for (let i = 2; i <= length; i++) {
    if (length % i == 0) {
      prime = true;
    }
  }
  return prime;
}



