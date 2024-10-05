  return lst.reduce((sum, num, i) => {
    if (i % 3 === 0) {
      return sum + num ** 2;
    } else if (i % 4 === 0) {
      return sum + num ** 3;
    } else {
      return sum;
    }
  }, 0);
}



