  let xNum = x.split("/")[0];
  let xDen = x.split("/")[1];
  let nNum = n.split("/")[0];
  let nDen = n.split("/")[1];

  return (xNum * nDen) % xDen === 0 && (nNum * xDen) % xDen === 0;
}



