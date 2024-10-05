const wordsString = (s) => {
  const regex = /\s*,\s*|\s+/;
  return s.split(regex);
}

