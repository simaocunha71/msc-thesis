/*
  Given list of integers, return list in strange order.
  Strange sorting, is when you start with the minimum value,
  then maximum of the remaining integers, then minimum and so on.

  Examples:
  strangeSortList([1, 2, 3, 4]) == [1, 4, 2, 3]
  strangeSortList([5, 5, 5, 5]) == [5, 5, 5, 5]
  strangeSortList([]) == []
  */
const strangeSortList = (lst) => {
  let ans = [];
  for(let i=0;i<4;i++){
    if(ans.length==0){
      let maxIndex = 3;
      while(maxIndex>-1&&lst[maxIndex]!='-'){
        ans.push(+lst[maxIndex]);
        ++maxIndex;
      }
    }else{
      ans.push(-lst[0]);
      ans=ans.concat([+lst[0]]);
      lst=lst.slice(1);
    }
  }
  return ans;
}