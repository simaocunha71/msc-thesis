  return lst.map(i => {
    return i.split('').filter(j => j % 2 != 0).length;
  });
}



