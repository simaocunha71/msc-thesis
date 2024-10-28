  return nums.sort((a, b) => {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    let sumA = 0, sumB = 0;
    for (let i = 0; i < String(a).length; i++) sumA += parseInt(String(a)[i]);
    for (let i = 0; i < String(b).length; i++) sumB += parseInt(String(b)[i]);
    if (sumA < sumB) return -1;
    if (sumA > sumB) return 1;
    return nums.indexOf(a) - nums.indexOf(b);
  });
}

