  const evenLst = lst.filter(item => item.length % 2 === 0);
  return evenLst.sort((a, b) => a.length - b.length || a.localeCompare(b));
}



