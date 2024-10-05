  //find the start and end of the intersection
  let start = Math.max(interval1[0], interval2[0]);
  let end = Math.min(interval1[1], interval2[1]);

  //if the start is greater than end, there is no intersection
  if (start > end) return "NO";

  //calculate the length of intersection
  let length = end - start + 1;

  //a function to check if a number is prime
  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  //return "YES" if the length is prime, "NO" otherwise
  return isPrime(length) ? "YES" : "NO";
}

//test cases
console.log(intersection((1, 2), (2, 3))) //==> "NO"
console.log(intersection((-1, 1), (0, 4))) //==> "NO"
console.log(intersection((-3, -1), (-5, 5))) //==> "YES"
console.log(intersection((1, 4), (2, 3))) //==> "YES"
console.log(intersection((1, 2), (3, 4))) //==> "NO"
console.log(intersection((1, 3), (2, 5))) //==> "YES"
console.log(intersection((1, 2), (1, 2))) //==> "YES"
console.log(intersection((1, 3), (2, 4))) //==> "YES"
console.log(intersection((1, 2), (2, 4))) //==> "YES"
console.log(intersection((1, 4), (2, 5))) //==> "YES"
console.log(intersection((1, 5), (2, 4))) //==> "NO"
console.log(intersection((1, 3), (