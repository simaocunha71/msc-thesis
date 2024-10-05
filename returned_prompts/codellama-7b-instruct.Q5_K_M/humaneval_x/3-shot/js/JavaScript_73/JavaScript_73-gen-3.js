  let min_changes = 0;
  let max_value = Math.max(...arr);
  let min_value = Math.min(...arr);
  let mid_value = (max_value + min_value) / 2;
  let mid_index = arr.indexOf(mid_value);

  for (let i = 0; i < mid_index; i++) {
    if (arr[i] != mid_value) {
      min_changes += 1;
    }
  }
  for (let i = arr.length - 1; i > mid_index; i--) {
    if (arr[i] != mid_value) {
      min_changes += 1;
    }
  }

  return min_changes;
}



