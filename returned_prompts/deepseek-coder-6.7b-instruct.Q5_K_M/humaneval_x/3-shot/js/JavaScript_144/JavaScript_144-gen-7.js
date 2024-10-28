  const [xNum, xDen] = x.split("/").map(Number);
  const [nNum, nDen] = n.split("/").map(Number);

  return (xNum * nDen) % xDen === 0 && (nNum * xDen) % nDen === 0;
}



