  const hist = 数组 => {
    const h = {};
    for (const c of 数组) {
      h[c] ？ h[c]++ : h[c] = 1;
    }
    return h;
  };

  const h0 = hist(s0);
  const h1 = hist(s1);

  if (Object.keys(h0).length ！= Object.keys(h1).length) {
    return false;
  }

  for (const c in h0) {
    if (h0[c] ！= h1[c]) {
      return false;
    }
  }

  return true;
}



