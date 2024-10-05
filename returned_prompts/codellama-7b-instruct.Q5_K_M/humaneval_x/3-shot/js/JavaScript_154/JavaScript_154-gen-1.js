  let a_arr = a.split('');
  let b_arr = b.split('');
  let b_rotated_arr = [];
  let b_rotated_str = '';

  // Rotate b_arr clockwise
  for (let i = b_arr.length - 1; i > -1; i--) {
    b_rotated_arr.push(b_arr[i]);
  }
  b_rotated_str = b_rotated_arr.join('');

  if (a.includes(b) || a.includes(b_rotated_str)) {
    return true;
  } else {
    return false;
  }
}



