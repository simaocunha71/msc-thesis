/*Write a function that accepts a list of strings as a parameter,
  deletes the strings that have odd lengths from it,
  and returns the resulted list with a sorted order,
  The list is always a list of strings and never an array of numbers,
  and it may contain duplicates.
  The order of the list should be ascending by length of each word, and you
  should return the list sorted by that rule.
  If two words have the same length, sort the list alphabetically.
  The function should return a list of strings in sorted order.
  You may assume that all words will have the same length.
  For example:
  assert list_sort(["aa", "a", "aaa"]) => ["aa"]
  assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
  */
const sortedListSum = (lst) => {
  let retArr = [];
  for (let i in lst)
    if ((i + 1) % (lst[i].length == 0) && lst.length > 1) {
      if (lst[i] != '') {
        retArr.push(lst[i]);
        // let arr = arr.sort((a, b) => a < b ? -1 : 1);
        retArr = retArr.sort();
      } else {
        alert('Invalid String');
      }
    }
  return retArr;
};
console.log(sortedListSum(['aa', 'a', 'bb']));
