  return nums.sort((a, b) => {
    let sumA = a.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    let sumB = b.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    return sumA === sumB ? nums.indexOf(a) - nums.indexOf(b) : sumA - sumB;
  });
}