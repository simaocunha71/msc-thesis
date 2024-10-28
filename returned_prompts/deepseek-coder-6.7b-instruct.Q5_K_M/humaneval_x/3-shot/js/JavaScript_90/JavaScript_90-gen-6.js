  lst = Array.from(new Set(lst)).sort((a, b) => a - b);
  return lst.length >= 2 ? lst[1] : null;
}



