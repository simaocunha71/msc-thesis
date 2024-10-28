const sortArray = (arr) => arr.sort(
  (a, b) =>
    (b.toString(2).match(/1/g) || []).length -
    (a.toString(2).match(/1/g) || []).length || a - b
);
