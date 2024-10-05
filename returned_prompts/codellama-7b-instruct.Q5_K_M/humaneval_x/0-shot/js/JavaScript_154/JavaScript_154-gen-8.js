/*
  a = "abcd"
  b = "abd"
  return false
  */
  const bArr = b.split('');
  const bRev = bArr.reverse().join('');
  const revA = a.split('').reverse().join('');
  let flag = false;
  let aLen = a.length;
  let bLen = b.length;
  let bRevLen = bRev.length;
  
  while (aLen > 0) {
    if (a.includes(b) || a.includes(bRev) || a.includes(bArr.join('')) || a.includes(bRevArr.join(''))) {
      return true;
    } else {
      a = a.slice(1);
      aLen--;
    }
  }
  return false;
}

