function list_sort(list){
  let sortedList = list.sort((a,b) => a.length - b.length);
  let oddList = sortedList.filter(item => item.length % 2 !== 0);
  let newList = sortedList.filter(item => item.length % 2 === 0);
  let sortedOddList = oddList.sort((a,b) => a.localeCompare(b));
  let sortedNewList = newList.sort((a,b) => a.localeCompare(b));
  let resultList = [].concat(sortedOddList,sortedNewList);
  return resultList;
}

