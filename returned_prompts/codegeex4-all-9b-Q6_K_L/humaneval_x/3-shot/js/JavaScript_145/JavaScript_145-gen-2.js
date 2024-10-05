  return nums.sort((a, b) => {
    let sumA = a.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    let sumB = b.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);

    if (sumA < sumB) {
      return -1;
    } else if (sumA > sumB) {
      return 1;
    } else {
      return nums.indexOf(a) - nums.indexOf(b);
    }
  });
}