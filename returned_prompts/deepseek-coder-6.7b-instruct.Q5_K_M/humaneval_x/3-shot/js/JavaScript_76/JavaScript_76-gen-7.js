  let power = 1;
  while(power < x) {
    power *= n;
    if(power === x) {
      return true;
    }
  }
  return false;
}



