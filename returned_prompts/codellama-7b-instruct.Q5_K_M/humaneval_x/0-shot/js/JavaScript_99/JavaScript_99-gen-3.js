/*
  Solution 1:
  let num = parseInt(value);
  if (value === num.toString()) {
    return num;
  } else {
    if (num > 0) {
      return num + 1;
    } else {
      return num - 1;
    }
  }
  */

B:
/*
  Solution 2:
  const num = parseInt(value);
  const diff = Math.abs(value - num);
  if (diff > 0.5) {
    return num + (num > 0 ? 1 : -1);
  }
  return num;
  */

C:
/*
  Solution 3:
  return parseFloat(value) < 0 ? Math.ceil(value) : Math.floor(value);
  */

D:
/*
  Solution 4:
  return parseInt(value + (value % 1 > 0.5 ? 1 : 0));
  */

E:
/*
  Solution 5:
  return Math.round(value);
  */

F:
/*
  Solution 6:
  return parseInt(value);
  */

G:
/*
  Solution 7:
  return Math.round(value);
  */

H:
/*
  Solution 8:
  return parseInt(value + (value % 1 > 0.5 ? 1 : 0));
  */

I:
/*
  Solution 9:
  return Math.round(value);
  */

J:
/*
  Solution 10:
  return parseInt(value);
  */

K:
/*
  Solution 11:
  return Math.round(value);
  */

L:
/*
  Solution 12:
  return parseInt(value + (value % 1 > 0.5 ? 1 : 0));
  */

M:
/*
  Solution 13:
  return parseInt(value);
  */

N:
/*
  Solution 14:
  return Math.round(value);
  */

O:
