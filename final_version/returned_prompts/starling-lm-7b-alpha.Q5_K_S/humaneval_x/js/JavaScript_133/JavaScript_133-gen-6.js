  lst.forEach(number => number = Math.ceil(number));
  return lst.reduce((sum, number) => sum + (number * number), 0);
}



