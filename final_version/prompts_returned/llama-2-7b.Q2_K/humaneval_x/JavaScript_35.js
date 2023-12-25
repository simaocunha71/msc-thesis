/*Return maximum element in the list.
  >>> maxElement([1, 2, 3])
  3
  >>> maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
  123
  */
const maxElement = (l) => {
  let n = l.length;
  for(let i=l.length-1;i>=0 ;i--){
    const element = l[i];
    if(element > max)max = element;
    else{
      return max;
    }
  }return max;
}