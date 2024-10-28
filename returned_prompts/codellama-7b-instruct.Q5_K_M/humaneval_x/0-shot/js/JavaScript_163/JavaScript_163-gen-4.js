  return [a, b].sort((a, b) => a - b).filter((n) => n % 2 === 0);

B:
  return [a, b].sort((a, b) => a - b).filter((n) => n % 2 === 0).map((n) => n);

C:
  const sorted = [a, b].sort((a, b) => a - b);
  const filtered = sorted.filter((n) => n % 2 === 0);
  return filtered;

D:
  return [a, b].sort((a, b) => a - b).filter(n => n % 2 === 0).map(n => n);

E:
  return [a, b].sort((a, b) => a - b).filter(n => n % 2 === 0).map(n => n);

F:
  const sorted = [a, b].sort((a, b) => a - b);
  const filtered = sorted.filter(n => n % 2 === 0);
  return filtered;

G:
  const sorted = [a, b].sort((a, b) => a - b);
  const filtered = sorted.filter(n => n % 2 === 0);
  return filtered.map(n => n);

H:
  return [a, b].sort((a, b) => a - b).filter(n => n % 2 === 0).map(n => n);

I:
  return [a, b].sort((a, b) => a - b).filter(n => n % 2 === 0).map(n => n);

J:
  const sorted = [a, b].sort((a, b) => a - b);
  const filtered = sorted.filter(n => n % 2 === 0);
  return filtered.map(n => n);

K:
  return [a, b].sort((a, b) => a - b).filter(n => n % 2 === 0).map(n => n);

L:
  return [a, b].sort((a, b) => a - b).filter