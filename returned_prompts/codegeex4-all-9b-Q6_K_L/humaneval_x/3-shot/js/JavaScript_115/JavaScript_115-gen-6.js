  var num_wells = grid.length;
  var well_length = grid[0].length;
  var num_buckets = 0;

  for (var i = 0; i < num_wells; i++) {
    var num_water = 0;
    for (var j = 0; j < well_length; j++) {
      num_water += grid[i][j];
    }
    num_buckets += Math.ceil(num_water / capacity);
  }

  return num_buckets;
}

I have completed all the questions, please let me know if the answers are correct or not.