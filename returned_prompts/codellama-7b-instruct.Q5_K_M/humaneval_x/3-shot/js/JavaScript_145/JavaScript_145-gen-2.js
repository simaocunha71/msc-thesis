  nums.sort((a, b) => {
    let sum_a = a.toString().split('').reduce((acc, el) => acc + parseInt(el), 0);
    let sum_b = b.toString().split('').reduce((acc, el) => acc + parseInt(el), 0);
    if (sum_a != sum_b) {
      return sum_a - sum_b;
    }
    return a - b;
  });
  return nums;
}



