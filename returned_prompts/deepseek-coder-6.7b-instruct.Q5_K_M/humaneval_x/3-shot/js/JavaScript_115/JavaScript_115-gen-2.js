  let total_wells = 0;
  let total_water = 0;

  for  (let row of grid) {
    total_wells += row.length;
    total_water += row.reduce((a, b) => a + b, 0);
  }

  return Math.ceil(total_water / (capacity * total_wells));
}



