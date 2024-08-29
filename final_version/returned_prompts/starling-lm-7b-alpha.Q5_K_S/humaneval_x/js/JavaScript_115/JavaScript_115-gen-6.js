  const max_row_units = grid.map(row => row.reduce((a, b) => a + b));
  const max_row_units_index = max_row_units.map((unit, index) => {
    let current_unit = unit;
    let current_index = index;
    while (current_unit > 0) {
      current_unit -= capacity;
      current_index += 1;
    }
    return current_index;
  });
  const result = max_row_units_index.reduce((a, b) => a + b, 0);
  return result;
}



