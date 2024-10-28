  for (let i = 1; ; i++) {
    if (Math.pow(i, 3) === a) {
      return true;
    }
    if (Math.pow(i, 3) > a) {
      return false;
    }
  }
} // This function can be optimized by using Math.sqrt() and Math.ceil() but it is not necessary for this problem.