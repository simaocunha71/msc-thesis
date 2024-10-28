```
const triangleArea = (a, b, c) => {
  if (a + b <= c || a + c <= b || b + c <= a) return -1;
  const s = (a + b + c) / 2;
  const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return Math.round(area * 100) / 100;
};
```