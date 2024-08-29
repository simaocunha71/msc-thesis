  const rotate = (s) => {
    return s.slice(1) + s.charAt(0);
  };
  for (let i = 0; i < a.length; i++) {
    if (a.indexOf(b, i) > -1) {
      return true;
    }
    if (b.length == 1) {
      break;
    }
    if (b.indexOf(b.charAt(0)) > -1) {
      return true;
    }
    b = rotate(b);
  }
  return false;
}



