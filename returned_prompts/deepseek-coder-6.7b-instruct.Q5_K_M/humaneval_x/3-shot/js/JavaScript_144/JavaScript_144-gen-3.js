  const [xNum, xDen] = x.split('/').map(Number);
  const [nNum, nDen] = n.split('/').map(Number);

  return (xNum * nNum) % (xDen * nDen) === 0;
}



