  return nums.sort((a, b) => {
    let sumA = a.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    let sumB = b.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    if (sumA === sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    } else {
      return sumA - sumB;
    }
  });
}