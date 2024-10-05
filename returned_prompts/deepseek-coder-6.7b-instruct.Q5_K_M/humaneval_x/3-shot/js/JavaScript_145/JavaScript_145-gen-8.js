  return nums.sort((a, b) => {
    let aDigitsSum = a.toString().split('').reduce((sum, digit) => sum + Math.abs(parseInt(digit)), 0);
    let bDigitsSum = b.toString().split('').reduce((sum, digit) => sum + Math.abs(parseInt(digit)), 0);
    return aDigitsSum - bDigitsSum || nums.indexOf(a) - nums.indexOf(b);
  });
}



