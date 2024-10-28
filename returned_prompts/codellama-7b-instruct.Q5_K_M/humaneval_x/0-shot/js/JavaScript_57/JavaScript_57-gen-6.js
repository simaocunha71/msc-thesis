
// if (l[i] < l[i+1])
//   return true;

// return false;

  // return l.every((e, i) => i === 0 || e >= l[i-1]);

  // return l.every((e, i) => i === 0 || e <= l[i-1]);

B:
  // return l.reduce((acc, e, i) => acc && i === 0 || e >= l[i-1], true);

  // return l.reduce((acc, e, i) => acc && i === 0 || e <= l[i-1], true);

C:
  // return l.reduce((acc, e, i) => (i === 0 || e >= l[i-1]) && acc, true);

  // return l.reduce((acc, e, i) => (i === 0 || e <= l[i-1]) && acc, true);

D:
  // return l.every((e, i) => i === 0 || e >= l[i-1]);

  // return l.every((e, i) => i === 0 || e <= l[i-1]);

E:
  return l.every((e, i, l) => i === 0 || (e >= l[i-1]));

  return l.every((e, i, l) => i === 0 || (e <= l[i-1]));

F:
  return l.every((e, i, l) => i === 0 || (e >= l[i-1]));

  return l.every((e, i, l) => i === 0 || (e <= l[i-1]));

G:
  return l.every((e, i, l) => i === 0 || (e >= l[i-1]));

  return l.every((e, i, l) => i === 0 || (e <= l[i-1]));

H:
  return l.every((e, i, l) => i === 0 || (e >= l[i-1]));

  return l.every((e,