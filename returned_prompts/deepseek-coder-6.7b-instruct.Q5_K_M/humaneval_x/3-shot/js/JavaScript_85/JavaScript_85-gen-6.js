  return lst.filter((_, idx) => idx % 2 === 1 && lst[idx] % 2 === 0).reduce((acc, cur) => acc + cur, 0);
}



