  let ordered_nums = [];
  let num_map = {};
  let num_sums = {};

  for (const num of nums) {
    num_map[num] = num;
    num_sums[num] = 0;

    let str_num = String(num);
    for (const char of str_num) {
      num_sums[num] += parseInt(char);
    }
  }

  for (const num of nums) {
    ordered_nums.push(num_map[num_sums[num]]);
  }

  return ordered_nums;
}



