const totalMatch = (lst1, lst2) => {
  return lst1.reduce((acc, word) => acc + word.length, 0) < lst2.reduce((acc, word) => acc + word.length, 0)
    ? lst1
    : lst2;
};

B:
const totalMatch = (lst1, lst2) => {
  const lengths = lst1.map(word => word.length);
  return lengths.reduce((acc, length) => acc + length, 0) <
    lengths.map(length => lst2.find(word => word.length === length)).reduce((acc, word) => acc + word.length, 0)
    ? lst1
    : lst2;
};

C:
const totalMatch = (lst1, lst2) => {
  const lengths = lst1.map(word => word.length);
  return lengths.reduce((acc, length) => acc + length, 0) <
    lengths.map(length => lst2.find(word => word.length === length)).reduce((acc, word) => acc + word.length, 0)
    ? lst1
    : lst2;
};

D:
const totalMatch = (lst1, lst2) => {
  const lengths = lst1.map(word => word.length);
  return lengths.reduce((acc, length) => acc + length, 0) <
    lengths.map(length => lst2.find(word => word.length === length)).reduce((acc, word) => acc + word.length, 0)
    ? lst1
    : lst2;
};

E:
const totalMatch = (lst1, lst2) => {
  const lengths = lst1.map(word => word.length);
  return lengths.reduce((acc, length) => acc + length, 0) <
    lengths.map(length => lst2.find(word => word.length === length)).reduce((acc, word) => acc + word.length, 0)
    ? lst1
    : lst2;
};
