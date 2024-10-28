const list_sort = (list) => {
  const oddLengths = [];
  const evenLengths = [];
  const sortedList = [];

  // Separate words into odd and even lengths
  for (word of list) {
    if (word.length % 2) oddLengths.push(word);
    else evenLengths.push(word);
  }

  // Sort odd lengths and even lengths by length and alphabetically
  oddLengths.sort((a, b) => (a.length - b.length) || a.localeCompare(b));
  evenLengths.sort((a, b) => (a.length - b.length) || a.localeCompare(b));

  // Concat sorted lists and return
  return sortedList.concat(oddLengths).concat(evenLengths);
};

  // Sort list alphabetically
  // const sortedList = list.sort((a, b) => a.localeCompare(b));

  // Return sorted list
  // return sortedList;
};

const list = ["aa", "a", "aaa"];
console.log(list_sort(list)); // ["aa"]

const list2 = ["ab", "a", "aaa", "cd"];
console.log(list_sort(list2)); // ["ab", "cd"]

const list3 = ["ab", "a", "aaa", "cd", "bc"];
console.log(list_sort(list3)); // ["ab", "bc", "cd"]

const list4 = ["ab", "a", "aaa", "cd", "bc", "ac"];
console.log(list_sort(list4)); // ["ab", "ac", "bc", "cd"]

const list5 = ["ab", "a", "aaa", "cd", "bc", "ac", "bb"];
console.log(list_sort(list5)); // ["ab", "ac", "bc", "bb", "cd"]

const list6 = ["ab", "a", "aaa", "cd", "bc", "ac", "bb", "aa"];
console.log(list_sort(list6)); // ["ab", "ac", "