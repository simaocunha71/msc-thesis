  const [n1, d1] = x.split("/").map(Number);
  const [n2] = n.split("/").map(Number);

  return (n1 * n2) % d1 === 0;
}



