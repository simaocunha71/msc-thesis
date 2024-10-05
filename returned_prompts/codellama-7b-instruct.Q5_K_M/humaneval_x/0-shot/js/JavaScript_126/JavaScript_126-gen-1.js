
const isSorted = (lst) => {
  const sorted = lst.every((item, i) => (i === 0) || (item >= lst[i - 1]));
  const noDups = lst.every((item, i) => (i === 0) || (item !== lst[i - 1]));
  return sorted && noDups;
};

B:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item >= lst[i - 1]));
};

C:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item !== lst[i - 1]));
};

D:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item >= lst[i - 1]));
};

E:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item >= lst[i - 1]));
};

F:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item !== lst[i - 1]));
};

G:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item >= lst[i - 1]));
};

H:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item !== lst[i - 1]));
};

I:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item >= lst[i - 1]));
};

J:

const isSorted = (lst) => {
  return lst.every((item, i) => (i === 0) || (item !== lst[