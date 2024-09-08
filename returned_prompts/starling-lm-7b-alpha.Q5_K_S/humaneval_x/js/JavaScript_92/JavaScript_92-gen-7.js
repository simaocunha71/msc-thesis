  if (typeof(x) === 'number' && typeof(y) === 'number' && typeof(z) === 'number' &&
     Math.floor(x) === x && Math.floor(y) === y && Math.floor(z) === z) {
    return (x + y) === z || (x + z) === y || (y + z) === x;
  } else {
    return false;
  }
}



