/*This function takes a list l and returns a list l' such that
  l' is identical to l in the odd indicies, while its values at the even indicies are equal
  to the values of the even indicies of l, but sorted.
  >>> sortEven([1, 2, 3])
  [1, 2, 3]
  >>> sortEven([5, 6, 3, 4])
  [3, 6, 5, 4]
  */
const sortEven = (l) => {
  let i;
  for(i=0; i< l.length; i+=2){
    if (l[i] < l[i+1]) {
      [l[i], l[i+1]] = [l[i+1], l[i]];
    }
  }
  return l;
}
module.exports = sortEven;
