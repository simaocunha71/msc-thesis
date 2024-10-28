  return text.replace(/\s+/g, (match) => {
    return match.length > 1 ? '-' : '_';
  });
}
// or
const fixSpaces = (text) => {
  return text.replace(/\s+/g, (match) => {
    return match.length > 1 ? '-' : '_';
  }).replace(/\s+/g, '_');
}