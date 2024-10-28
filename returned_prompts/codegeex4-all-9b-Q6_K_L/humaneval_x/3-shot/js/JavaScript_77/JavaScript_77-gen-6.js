  let absA = Math.abs(a);
  if (a == 0) {
    return true;
  }
  for (let i = 1; i <= Math.floor(Math.sqrt(absA)); i++) {
    if (i * i * i == absA) {
      return true;
    }
  }
  return false;
}



