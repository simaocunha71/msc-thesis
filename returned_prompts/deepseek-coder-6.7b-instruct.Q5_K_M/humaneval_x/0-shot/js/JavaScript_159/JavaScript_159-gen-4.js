  let totalEaten = number;
  let eatenCarrots = need;
  if(eatenCarrots > remaining){
    totalEaten += remaining;
    eatenCarrots = remaining;
    remaining = 0;
  } else {
    totalEaten += eatenCarrots;
    remaining -= eatenCarrots;
  }
  
  return [totalEaten, remaining];
}

console.log(eat(5, 6, 10)) // -> [11, 4]
console.log(eat(4, 8, 9)) // -> [12, 1]
console.log(eat(1, 10, 10)) // -> [11, 0]
console.log(eat(2, 11, 5)) // -> [7, 0]

/*
  