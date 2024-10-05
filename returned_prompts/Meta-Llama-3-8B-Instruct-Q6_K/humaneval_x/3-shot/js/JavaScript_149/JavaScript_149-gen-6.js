  lst = lst.filter(function(x) {
    return x.length % 2 == 0;
  });
  lst.sort(function(a, b) {
    if (a.length == b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
  return lst;
}
// Note: This problem description is not accurate. The function should be named list_sort, not sortedListSum. It should also return a list of strings in sorted order, not the sum of the lengths of the strings.
// This is a revised version of the problem description:
// Write a function that accepts a list of strings as a parameter, deletes the strings that have odd lengths from it, and returns the resulted list in a sorted order. The list is always a list of strings and never an array of numbers, and it may contain duplicates. The order of the list should be ascending by length of each word, and you should return the list sorted by that rule. If two words have the same length, sort the list alphabetically. The function should return a list of strings in sorted order. For example: assert list_sort(["aa", "a", "aaa"]) => ["aa"] assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]



