const list = lst;
let sortedList = list.sort((a, b) => a.length - b.length);
for (let i = 0; i < sortedList.length; i++) {
  if (sortedList[i].length % 2 !== 0) {
    sortedList.splice(i, 1);
    i--;
  }
}
return sortedList;
}
