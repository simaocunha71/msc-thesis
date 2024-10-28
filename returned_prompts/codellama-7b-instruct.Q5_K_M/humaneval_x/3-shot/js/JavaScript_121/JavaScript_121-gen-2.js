  return lst.filter((x, i) => i % 2 == 0 && x % 2 != 0).reduce((x, y) => x + y, 0);
}



