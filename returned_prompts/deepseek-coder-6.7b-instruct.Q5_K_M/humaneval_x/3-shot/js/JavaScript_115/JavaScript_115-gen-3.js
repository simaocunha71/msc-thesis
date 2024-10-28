  let total_wells = 0;
  let total_water = 0;

  for  (let i  in grid)  {
    for  (let j  in grid[i])  {
      if  (grid[i][j]  ！= 0)  {
        total_wells++;
        total_water++;
       }
     }
   }

  return Math.ceil(total_water  /  capacity) * total_wells;
}



