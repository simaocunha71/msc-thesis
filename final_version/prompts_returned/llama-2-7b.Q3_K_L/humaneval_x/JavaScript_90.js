/*
  You are given a list of integers.
  Write a function nextSmallest() that returns the 2nd smallest element of the list.
  Return null if there is no such element.
  
  nextSmallest([1, 2, 3, 4, 5]) == 2
  nextSmallest([5, 1, 4, 3, 2]) == 2
  nextSmallest([]) == null
  nextSmallest([1, 1]) == null
  */
const nextSmallest = (lst) => {
  if(lst.length === 0){
    return null;
  } else if(typeof lst[1] !== 'number'){
      throw new Error('array must contain numbers');
    }
  
  let index, minIndex;
  for(let i = 2;i < lst.length; i++){
      const element = lst[i];
      if(element < lst[minIndex]){
          minIndex++;
          if(minIndex === i){
              return element;
          } else {
              index = minIndex + 1;
              nextSmallest(lst.splice(index, 1));
          }
      } else {
          if(minIndex !== i) {
            nextSmallest(lst.splice(minIndex, 1));
          }
        return lst[i];  
      }
    }
}

console.log(nextSmallest([5, 3, 4, 2, 1])); //5
console.log(nextSmallest([4, 5, 6, 7, 8])); //0 (no next smallest)