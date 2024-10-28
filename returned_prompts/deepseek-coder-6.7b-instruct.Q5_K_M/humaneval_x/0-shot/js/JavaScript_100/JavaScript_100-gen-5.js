  let stones = [n];
  let nextStone = n;

  for(let i = 1; i < n; i++){
    if(nextStone % 2 === 0){
      nextStone = nextStone + 2;
    } else {
      nextStone = nextStone + 2;
    }
    stones.push(nextStone);
  }

  return stones;
}

console.log(makeAPile(3)); // [3, 5, 7]

*/

/*

