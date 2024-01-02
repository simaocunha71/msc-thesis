/*
  You are given a 2 dimensional data, as a nested lists,
  which is similar to matrix, however, unlike matrices,
  each row may contain a different number of columns.
  Given lst, and integer x, find integers x in the list,
  and return list of tuples, [(x1, y1), (x2, y2) ...] such that
  each tuple is a coordinate - (row, columns), starting with 0.
  Sort coordinates initially by rows in ascending order.
  Also, sort coordinates of the row by columns in descending order.
  
  Examples:
  getRow([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
  ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
  getRow([], 1) == []
  getRow([[], [1], [1, 2, 3]], 3) == [(2, 2)]
  */
const getRow = (lst, x) => {
  const map = new Map();
  for(let i in lst){ // add to map all the rows of first dimension
    for(i in lst[0]){
      if(!map.has([i, 0])){ // create array with coordinates [i, 0]
        map.set([i, 0], []); // set coordinates to empty arrays
      }
      if(!map.has([i, 1])){ // add to empty array in previous coordinate
        map.get([i, 0]).push([]); // new row of coordinates
      }
    }
  }
  let res = [];
  for (let j in lst[0]) { // iterate through each row and put it in a list
    if(!map.has([j, 1])){ // check if this coordinate is yet to add
      map.set([j, 1], []); // add empty array to coordinates
    }
  
    let curr = []; // create an empty list for each coordinates
    res = res