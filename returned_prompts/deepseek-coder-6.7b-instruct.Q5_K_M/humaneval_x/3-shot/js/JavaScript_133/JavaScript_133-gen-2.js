  return lst.reduce((sum, num) => {
    return sum + Math.pow(Math.ceil(num), 2);
  }, 0);
}



