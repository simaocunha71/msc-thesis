  const evenStrings = lst.filter(str => str.length % 2 === 0);
  return evenStrings.sort((a, b) => a.length - b.length || a.localeCompare(b));
}



