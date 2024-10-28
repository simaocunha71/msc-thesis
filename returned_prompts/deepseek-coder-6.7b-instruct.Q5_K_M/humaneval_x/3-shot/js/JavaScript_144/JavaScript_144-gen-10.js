  const [numX, denX] = x.split("/").map(Number);
  const [numN, denN] = n.split("/").map(Number);
  return (numX * numN) % (denX * denN) === 0;
}



