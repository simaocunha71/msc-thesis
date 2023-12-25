/*
  You are given a non-empty list of positive integers. Return the greatest integer that is greater than
  zero, and has a frequency greater than or equal to the value of the integer itself.
  The frequency of an integer is the number of times it appears in the list.
  If no such a value exist, return -1.
  Examples:
      search([4, 1, 2, 2, 3, 1])) == 2
      search([1, 2, 2, 3, 3, 3, 4, 4, 4])) == 3
      search([5, 5, 4, 4, 4])) == -1
  */
const search = (lst) => {
  let map = {};
  for(let i=0;i<lst.length;++i){
    if(!map[lst[i]]){//如果没有映射到就进行插入排序，然后找到最大值并把他当作权重的采样函数。
      const n = lst.length;
      let j = i, res = Number.MIN_VALUE;
      while(j<n) {//如果还没有找到，且这个值在这里的时候还可以被选中，那么就进行排序。
        if(lst[j]>res){
          res = lst[j];
          j++;
        }else {
            break;
        }
      }
    map[lst[i]]=1;
  }}

//如果没有找到，那么就返回-1即可。
if(map.hasOwnProperty('6')){res=(Number.MAX_VALUE/2)}else return -1;}