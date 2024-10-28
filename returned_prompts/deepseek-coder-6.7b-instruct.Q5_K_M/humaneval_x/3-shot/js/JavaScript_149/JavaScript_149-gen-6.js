  lst.sort((a, b) => {
    if  (a.length  != b.length)  {
      return a.length  - b.length;
    } else  {
      return a.localeCompare(b);
    }
  });

  return lst.filter(word => word.length  % 2 === 0);
}



