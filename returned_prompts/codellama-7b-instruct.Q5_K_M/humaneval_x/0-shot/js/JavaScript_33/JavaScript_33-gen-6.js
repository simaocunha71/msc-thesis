/*This function takes a list l and returns a list l' such that
  l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
  to the values of the corresponding indicies of l, but sorted.
  >>> sortThird([1, 2, 3])
  [1, 2, 3]
  >>> sortThird([5, 6, 3, 4, 8, 9, 2])
  [2, 6, 3, 4, 8, 9, 5]
  */
const sortThird = (l) => {
    return l.map((item, index) => {
        if (index % 3 === 0) {
            return l.slice(index, index + 3).sort()[0];
        } else {
            return item;
        }
    });
};
