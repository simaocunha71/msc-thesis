  for (let i = 0; i < b.length; i++) {
    let temp = b.substring(i) + b.substring(0, i);
    if (a.indexOf(temp) > -1) {
      return true;
    }
  }
  return false;
}



