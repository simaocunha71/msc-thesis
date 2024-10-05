  for (let i = 0; i < a.length; i++) {
    const rotation = a.slice(i) + a.slice(0, i);
    if (rotation.includes(b)) {
      return true;
    }
  }
  return false;
}



