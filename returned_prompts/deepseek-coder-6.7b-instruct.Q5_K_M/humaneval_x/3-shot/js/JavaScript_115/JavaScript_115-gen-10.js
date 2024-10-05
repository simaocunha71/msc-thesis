  let total = 0;
  for  (let row of grid) 
    for  (let cell of row) 
      total += cell;

  return Math.ceil(total / capacity);
}



