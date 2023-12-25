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
  if ((a === 0 || a % 1 != 3)) return false;
  let b2 = Math.pow(6, Math.floor(Math.abs(a / 6)));
  return (b2 >= 1 && b2 <= 64);
};
export default iscube;