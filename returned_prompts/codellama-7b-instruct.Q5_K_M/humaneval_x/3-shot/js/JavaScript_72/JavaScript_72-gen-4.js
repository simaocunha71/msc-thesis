  if (q.length < 1) {
    return false;
  }
  if (q.join('') == q.reverse().join('')) {
    if (q.reduce((a,b) => a + b) <= w) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}



