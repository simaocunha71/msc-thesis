  const numsClone = nums.map(num => num);
  numsClone.sort((a, b) => {
    const sumA = numsClone.findIndex(num => num === a);
    const sumB = numsClone.findIndex(num => num === b);
    if (sumA < sumB) {
      return -1;
    } else if (sumA > sumB) {
      return 1;
    } else {
      const sumAstr = a.toString();
      const sumBstr = b.toString();
      let sumAnum = 0;
      let sumBnum = 0;
      for (let i = 0; i < sumAstr.length; i++) {
        sumAnum += +sumAstr[i];
      }
      for (let i = 0; i < sumBstr.length; i++) {
        sumBnum += +sumBstr[i];
      }
      if (sumAnum < sumBnum) {
        return -1;
      } else if (sumAnum > sumBnum) {
        return 1;
      } else {
        return 0;
      }
    }
  });
  return nums;
}



