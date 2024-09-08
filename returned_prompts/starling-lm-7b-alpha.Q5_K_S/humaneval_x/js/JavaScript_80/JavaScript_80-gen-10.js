  if (s.length < 3) return false;
  return (new Set(s.slice(0, 3))).size == 3;
}



