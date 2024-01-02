/* Given a string, find out how many distinct characters (regardless of case) does it consist of
  >>> countDistinctCharacters('xyzXYZ')
  3
  >>> countDistinctCharacters('Jerry')
  4
  */
const countDistinctCharacters = (string) => {
  const arr = string.split("");
  let totalUniqueElements = 0;
  for(let element of arr){
    if (!element || !element.toLowerCase()){
      continue;
    } else{
      totalUniqueElements += 1;
    }
  }
  return totalUniqueElements;
}