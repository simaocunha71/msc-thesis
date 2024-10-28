  return strings.filter(s => s.startsWith(prefix));
}
// OR
const filterByPrefix = (strings, prefix) => {
  return strings.filter(s => s.slice(0, prefix.length) === prefix);
}