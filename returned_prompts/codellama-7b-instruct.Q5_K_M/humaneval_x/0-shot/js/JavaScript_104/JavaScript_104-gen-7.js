const uniqueDigits = (x) => {
  return x.filter(i => !(i % 2)).sort((a,b) => a-b);
}

