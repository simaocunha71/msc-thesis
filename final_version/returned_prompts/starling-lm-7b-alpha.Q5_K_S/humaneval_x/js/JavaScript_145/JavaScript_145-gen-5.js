  const nums_original = [...nums];
  nums.sort((a, b) => {
    const sum_a = (+a+'').split('').reduce((acc, curr) => acc + +curr, 0);
    const sum_b = (+b+'').split('').reduce((acc, curr) => acc + +curr, 0);
    return sum_a != sum_b ? sum_a - sum_b : nums_original.indexOf(a) - nums_original.indexOf(b);
  });

  return nums;
}



