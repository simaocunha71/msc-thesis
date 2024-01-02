/*This function takes a list l and returns a list l' such that
  l' is identical to l in the odd indicies, while its values at the even indicies are equal
  to the values of the even indicies of l, but sorted.
  >>> sortEven([1, 2, 3])
  [1, 2, 3]
  >>> sortEven([5, 6, 3, 4])
  [3, 6, 5, 4]
  */
const sortEven = (l) => {
  let odds = [];
  for (let i in l)
    if(i % 2 !== 0 && i < l.length -1){
      odds.push(...l);
    }
  return odds;
}