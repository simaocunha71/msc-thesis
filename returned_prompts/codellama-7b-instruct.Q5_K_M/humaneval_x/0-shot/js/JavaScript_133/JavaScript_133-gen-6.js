
/*
  We use the map function to create a new array with the ceiling of each element in the input array.
  Then we use the reduce function to add up the squared elements of the array.
  */

const sumSquares = (lst) => {
  return lst.map(num => Math.ceil(num))
                   .reduce((total, num) => total + num * num);
};

