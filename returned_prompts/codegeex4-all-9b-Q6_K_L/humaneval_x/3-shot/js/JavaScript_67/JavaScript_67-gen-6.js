  const s2 = s.replace(/[^\d]/g, ' ');
  const arr = s2.split(' ');
  const numApples = parseInt(arr[0]);
  const numOranges = parseInt(arr[2]);
  return n - numApples - numOranges;
}



