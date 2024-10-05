  return lst.filter((num, index) => index % 2 !== 0 && num % 2 === 0).reduce((a, b) => a + b, 0);
}



