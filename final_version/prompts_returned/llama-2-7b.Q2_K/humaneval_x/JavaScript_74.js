/*
  Write a function that accepts two lists of strings and returns the list that has
  total number of chars in the all strings of the list less than the other list.

  if the two lists have the same number of chars, return the first list.

  Examples
  totalMatch([], []) ➞ []
  totalMatch(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
  totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
  totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
  totalMatch(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
  */
const totalMatch = (lst1, lst2) => {
  let ret = [];
  for (let i = 0; i < lst2.length; ++i) {
    if (!lst1[i].includes(lst2[i])) return lst2;
    let count = lst1[i].indexOf(lst2[i]);
    if (count > -1 && ret.every((el, indx) => el == '')) {
      ++ret.length;
      ret[ret.length] = lst1[i];
    }
  }
  return lst1.filter((el, indx) => !!ret[indx]);
};
