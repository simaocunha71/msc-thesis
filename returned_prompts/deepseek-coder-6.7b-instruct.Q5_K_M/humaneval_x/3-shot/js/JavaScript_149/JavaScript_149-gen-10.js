  return lst
    .filter((str) => str.length % 2 === 0)
    .sort((a, b) => a.length - b.length || a.localeCompare(b))
}



