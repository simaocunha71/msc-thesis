  const length = string.length;
  for (let i = 2; i <= length; i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
}  // This function is not efficient for large strings. For larger strings, you might want to use a more efficient algorithm for checking if a number is prime.