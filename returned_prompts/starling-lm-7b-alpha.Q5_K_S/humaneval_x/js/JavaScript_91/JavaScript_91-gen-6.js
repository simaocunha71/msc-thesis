  const S_array = S.split(/\s+/);
  let count = 0;
  for (let i = 0; i < S_array.length; i++) {
    if (S_array[i] == 'I') {
      if (S_array[i + 1] == '.' || S_array[i + 1] == '?' || S_array[i + 1] == '!') {
        count += 1;
      }
    }
  }
  return count;
}



