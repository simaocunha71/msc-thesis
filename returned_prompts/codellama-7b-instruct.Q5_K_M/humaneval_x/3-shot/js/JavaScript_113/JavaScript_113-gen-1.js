  return lst.map(str => {
    return str.split('').filter(x => {
      if (x % 2 != 0) {
        return x;
      }
    }).length;
  });
}



