  let total_wells = 0;
  let total_buckets = 0;

  for  (const row of grid)  {
    for  (const well of row)  {
      total_wells += well;
     }
   }

  total_buckets = total_wells / capacity;
  return Math.ceil(total_buckets);
}



