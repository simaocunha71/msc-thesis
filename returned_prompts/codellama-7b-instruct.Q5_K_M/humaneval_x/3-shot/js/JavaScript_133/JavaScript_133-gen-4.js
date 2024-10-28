  return lst.map((num) => Math.ceil(num)).map((num) => num ** 2).reduce((sum, num) => sum + num, 0);
}



