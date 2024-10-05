  let xNum = parseInt(x.split('/')[0]);
  let xDen = parseInt(x.split('/')[1]);
  let nNum = parseInt(n.split('/')[0]);
  let nDen = parseInt(n.split('/')[1]);

  let newXNum = xNum * nDen;
  let newXDen = xDen * nNum;

  return newXNum % newXDen === 0;
}



