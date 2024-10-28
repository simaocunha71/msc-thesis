  var result = nums.slice();
  result.sort((a, b) => {
    let asum = (a + '').split('').reduce((acc, c) => acc + Number(c), 0);
    let bsum = (b + '').split('').reduce((acc, c) => acc + Number(c), 0);
    if (asum != bsum) return asum - bsum;
    else return a - b;
  });
  return result;
}



