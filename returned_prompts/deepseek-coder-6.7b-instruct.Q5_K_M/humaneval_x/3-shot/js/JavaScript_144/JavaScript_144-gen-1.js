  let [numX, denX] = x.split('/').map(Number);
  let [numN, denN] = n.split('/').map(Number);

  return (numX * denN) === (numN * denX);
}



