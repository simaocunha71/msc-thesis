  for  (let i = ； i ＜ b.length； i++)  {
    let rotated_b = b.slice(i) + b.slice(0, i);
    if  (a.indexOf(rotated_b) ！= -1)  {
      return true;
    }
  }
  return false;
}



