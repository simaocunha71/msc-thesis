/*
  Imagine a road that's a perfectly straight infinitely long line.
  n cars are driving left to right;  simultaneously, a different set of n cars
  are driving right to left.   The two sets of cars start out being very far from
  each other.  All cars move in the same speed.  Two cars are said to collide
  when a car that's moving left to right hits a car that's moving right to left.
  However, the cars are infinitely sturdy and strong; as a result, they continue moving
  in their trajectory as if they did not collide.

  This function outputs the number of such collisions.
  */
const carRaceCollision = (n) => {
  let numCollisions = 0;

  // Drives from left to right
  for (let i=1;i<998;i++)
    if(i%2!=0){
      numCollisions+=carRace(i-1,0);
    }else{numCollisions+=carRace(n+i-1,0);}
  // Drives from right to left
  for (let i=0;i<998;i++)
    if(i%2==0){
      numCollisions+=carRace(i+1,0);
    }else{numCollisions+=carRace(n-i-1,0);}
  
  return numCollisions;
};
