  return lst.reduce((sum, num) => {
    return sum + (Math.abs(num) % 2 === 1 ? Math.pow(num, 2) : 0);
  }, 0);
}



