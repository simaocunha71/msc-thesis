  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      if (i + j == n && i % 2 == 0 && j % 2 == 0) {
        return true;
      }
    }
  }
  return false;
}



