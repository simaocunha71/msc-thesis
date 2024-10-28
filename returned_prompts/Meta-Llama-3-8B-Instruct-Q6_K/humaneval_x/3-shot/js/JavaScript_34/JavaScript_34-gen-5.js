  return [...new Set(l)].sort((a, b) => a - b);
}
// Alternative solution
const unique = (l) => {
  return l.filter((item, index) => l.indexOf(item) === index).sort((a, b) => a - b);
} // This solution is less efficient for large lists
// Alternative solution with sorting
const unique = (l) => {
  return [...l.reduce((acc, current) => {
    if (!acc.includes(current)) {
      acc.push(current);
    }
    return acc;
  }, [])].sort((a, b) => a - b);
} // This solution is less efficient for large lists
// Alternative solution with Set and sort
const unique = (l) => {
  return Array.from(new Set(l)).sort((a, b) => a - b);
} // This solution is less efficient for large lists
// Alternative solution with Map
const unique = (l) => {
  return [...new Map(l.map(x => [x, true])).keys()].sort((a, b) => a - b);
} // This solution is less efficient for large lists
// Alternative solution with Array.from
const unique = (l) => {
  return Array.from(new Set(l)).sort((a, b) => a - b);
} // This solution is less efficient for large lists
// Alternative solution with Object.keys
const unique = (l) => {
  return Object.keys(new Map(l.map(x => [x, true]))).sort((a, b) => a - b);
} // This solution is less efficient for large lists
// Alternative solution with Object.values
const unique = (l) => {
  return Object.values(new Map(l.map(x => [x, true]))).sort((a, b) => a - b);
} // This solution is less efficient for large lists
// Alternative solution with Object.keys and Object.values
const unique = (l) => {
  return [...new Map(l.map(x => [x, true])).values()].sort((a, b) => a - b);
} // This solution is less efficient for large lists
// Alternative solution with Object.keys and Object.values
const unique = (l) => {
  return [...Object.keys(new Map(l.map(x => [x, true]))).map(x => l.find(y => y === x))].sort((a, b) => a - b);
} // This solution is less efficient for