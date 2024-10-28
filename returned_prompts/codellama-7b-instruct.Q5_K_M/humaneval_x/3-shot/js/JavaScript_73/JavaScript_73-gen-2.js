  let min_changes = Infinity;
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    let left_val = arr[left];
    let right_val = arr[right];

    if (left_val == right_val) {
      left += 1;
      right -= 1;
    } else {
      let left_diff = Math.abs(left_val - right_val);
      let right_diff = Math.abs(left_val - right_val);
      min_changes = Math.min(min_changes, left_diff + right_diff);
      left += 1;
      right -= 1;
    }
  }

  return min_changes;
}



