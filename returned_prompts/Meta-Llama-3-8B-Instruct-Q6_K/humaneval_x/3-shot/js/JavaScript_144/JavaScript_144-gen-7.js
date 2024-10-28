  let xNum = parseInt(x.split('/')[0]);
  let xDen = parseInt(x.split('/')[1]);
  let nNum = parseInt(n.split('/')[0]);
  let nDen = parseInt(n.split('/')[1]);

  let resultNum = xNum * nDen;
  let resultDen = xDen * nNum;

  if (resultNum % resultDen == 0) {
    return true;
  } else {
    return false;
  }
}
