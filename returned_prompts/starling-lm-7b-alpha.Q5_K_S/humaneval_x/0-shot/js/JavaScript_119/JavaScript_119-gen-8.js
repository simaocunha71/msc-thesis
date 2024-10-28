let l = lst[0];
let r = lst[1];
let c = 0;
let b = true;

for (let i = 0; i < l.length; i++) {
  if (l[i] === '(') {
    c++;
  } else {
    if (c === 0) {
      b = false;
    } else {
      c--;
    }
  }
}

if (c === 0 && b) {
  for (let i = r.length - 1; i >= 0; i--) {
    if (r[i] === '(') {
      c++;
    } else {
      if (c === 0) {
        b = false;
      } else {
        c--;
      }
    }
  }
}

if (b && c === 0) {
  return 'Yes';
} else {
  return 'No';
}

};

matchParens(["()(", ")"]);













































































































































































































































































