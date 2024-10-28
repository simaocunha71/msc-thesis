const totalMatch = (lst1, lst2) => {
  const total1 = lst1.reduce((acc, str) => acc + str.length, 0);
  const total2 = lst2.reduce((acc, str) => acc + str.length, 0);
  if (total1 === total2) return lst1;
  return total1 < total2 ? lst1 : lst2;
};

B:
const totalMatch = (lst1, lst2) => {
  const total1 = lst1.reduce((acc, str) => acc + str.length, 0);
  const total2 = lst2.reduce((acc, str) => acc + str.length, 0);
  return total1 < total2 ? lst1 : lst2;
};

C:
const totalMatch = (lst1, lst2) => {
  const total1 = lst1.reduce((acc, str) => acc + str.length, 0);
  const total2 = lst2.reduce((acc, str) => acc + str.length, 0);
  return total1 < total2 ? lst1 : lst2;
};

D:
const totalMatch = (lst1, lst2) => {
  const total1 = lst1.reduce((acc, str) => acc + str.length, 0);
  const total2 = lst2.reduce((acc, str) => acc + str.length, 0);
  return total1 < total2 ? lst1 : lst2;
};

E:
const totalMatch = (lst1, lst2) => {
  const total1 = lst1.reduce((acc, str) => acc + str.length, 0);
  const total2 = lst2.reduce((acc, str) => acc + str.length, 0);
  return total1 < total2 ? lst1 : lst2;
};

F:
const totalMatch = (lst1, lst2) => {
  const total1 = lst1.reduce((acc, str) => acc + str.length, 0);
  const total2 = lst2.reduce((acc, str) => acc + str.length, 0);
  return total1 < total2 ? lst