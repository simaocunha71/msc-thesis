  const evenNodes = arr.filter(node => node % 2 === 0);
  if (evenNodes.length === 0) {
    return [];
  }
  return [evenNodes[0], evenNodes.findIndex(node => node === evenNodes[0])];
}



