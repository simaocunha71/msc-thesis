/*This function takes a list l and returns a list l' such that
  l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
  to the values of the corresponding indicies of l, but sorted.
  >>> sortThird([1, 2, 3])
  [1, 2, 3]
  >>> sortThird([5, 6, 3, 4, 8, 9, 2])
  [2, 6, 3, 4, 8, 9, 5]
  */
const sortThird = (l) => {
  let res = [];
  for(let i=0;i<l.length; i++){
    if(!isDividedByThree(l[i]) && !res.includes(l[i])){
      res.push(l[i]);
    }
  }
  return res;
}
// Function to check whether number is divisible by three
const isDividedByThree = (num) => {
  if((num % 3) === 0){
    return true;
  }else{
    return false;
  }
};

module.exports = sortThird;