  const regex = /(\d+)\s*(?:apples)?\s*(?:and)?\s*(\d+)/;
  const match = s.match(regex);
  const apples = match[1] ? parseInt(match[1]) : 0;
  const oranges = match[2] ? parseInt(match[2]) : 0;

  return n - apples - oranges;
}



