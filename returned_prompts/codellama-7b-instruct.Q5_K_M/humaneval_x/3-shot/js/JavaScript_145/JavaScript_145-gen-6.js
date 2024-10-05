  let num_to_str_map = {};
  let num_to_sum_map = {};
  let num_to_index_map = {};

  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    let sum = 0;

    for (let c of String(num)) {
      sum += Number(c);
    }

    num_to_str_map[num] = String(num);
    num_to_sum_map[num] = sum;
    num_to_index_map[num] = i;
  }

  return Object.keys(num_to_sum_map)
    .sort((a, b) =>
      (num_to_sum_map[a] == num_to_sum_map[b])
        ? (num_to_index_map[a] - num_to_index_map[b])
        : (num_to_sum_map[a] - num_to_sum_map[b])
    )
    .map((x) => Number(num_to_str_map[x]));
}



