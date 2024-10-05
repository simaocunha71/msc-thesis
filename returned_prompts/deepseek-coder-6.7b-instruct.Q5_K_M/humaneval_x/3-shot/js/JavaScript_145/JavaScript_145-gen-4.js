  return nums.sort((a, b) => {
    let aSum = a.toString().split('').reduce((acc, cur) => acc + Math.abs(parseInt(cur)), 0);
    let bSum = b.toString().split('').reduce((acc, cur) => acc + Math.abs(parseInt(cur)), 0);

    return aSum - bSum || nums.indexOf(a) - nums.indexOf(b);
  });
}



