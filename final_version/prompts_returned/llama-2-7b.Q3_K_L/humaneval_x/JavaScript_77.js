/*
  Write a function that takes an integer a and returns true
  if this ingeger is a cube of some integer number.
  Note: you may assume the input is always valid.
  Examples:
  iscube(1) ==> true
  iscube(2) ==> false
  iscube(-1) ==> true
  iscube(64) ==> true
  iscube(0) ==> true
  iscube(180) ==> false
  */
const iscube = (a) => {
  if ((a === 0 || a < 0 ) && parseInt(a) !== 0 ){
    return false; // not an integer or negative so no cube
  } else {
    let cubedA = Math.pow(a,3);
    
    return (isint(cubedA));// is a cube of some int
  }
}
