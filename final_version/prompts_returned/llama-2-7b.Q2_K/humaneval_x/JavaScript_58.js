/*Return sorted unique common elements for two lists.
  >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
  [1, 5, 653]
  >>> common([5, 3, 2, 8], [3, 2])
  [2, 3]

  */
const common = (l1, l2) => {
  const isSameElement = (a, b) => a === b;
  
  let uniqueList = []; // unique elements of list 'l'
  let notUniqueList = []; // unique elements that are not in list 'l'

  for (let i = 0, l = Math.min(l1.length, l2.length); i < l; ++i) {
    const elementA = isSameElement(l1[i], l2[i]); // true when the two lists have the same element at index 'i'
  
    if (elementA && !uniqueList.includes(l1[i])) { // element A, and not unique yet in list 'l', push it to unique list
      uniqueList.push(l1[i]);
    } else if (!isSameElement(l1[i], l2[i]) && !notUniqueList.includes(l1[i])) { // element A, and not in list of 'uniques' yet
      notUniqueList.push(l1[i]);
    }
  }
  
  if (l1.length === l2.length) {
    return uniqueList;
  } else if (notUniqueList.length + uniqueList.length !== l1.length) { // 0, in either case of the above if, should be replaced by "!=" to avoid null conditions
    throw new RangeError('l1 and l2 are not the same length');
  } else if (uniqueList.length === l1.length && uniqueList[uniqueList.length - 1] == l1[l1.length]) { // the only one element in 'l' is also in unique list, throw