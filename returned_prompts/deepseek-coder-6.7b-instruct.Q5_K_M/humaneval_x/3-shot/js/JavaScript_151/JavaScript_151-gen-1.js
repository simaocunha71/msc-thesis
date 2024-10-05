  return lst.reduce((sum, num) => {
    if (num > 0 && Number.isInteger(num) && num % 2 !== 0) {
      return sum + num*num;
    }
    return sum;
  }, 0);
}



