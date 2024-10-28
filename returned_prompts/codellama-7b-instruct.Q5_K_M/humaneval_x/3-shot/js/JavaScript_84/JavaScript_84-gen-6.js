  return (N >>> 0).toString(2)
  .split('')
  .reduce((acc, cur) => acc + parseInt(cur), 0)
  .toString();
}



