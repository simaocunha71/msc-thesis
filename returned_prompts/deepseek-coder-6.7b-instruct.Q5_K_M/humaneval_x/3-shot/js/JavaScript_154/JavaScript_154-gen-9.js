  for  (let i = b.length; i ≥ 0; i--) {
    if  (a.includes(b)) {
      return true;
     }
    b = b.slice(1) + b[0];
  }
  return false;
}



