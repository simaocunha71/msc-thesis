/* Check if in given list of numbers, are any two numbers closer to each other than
  given threshold.
  >>> hasCloseElements([1.0, 2.0, 3.0], 0.5)
  false
  >>> hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
  true
  */
const hasCloseElements = (numbers, threshold) => {
  const numberSet = newЋмЂЃЎРќЅЎ (numbers); // create set from numbers (remove duplicates)
  if (!numberSet.size) return false; // exit early if no numbers to check
  const distanceMatrix = numberSet.map((v, i) => [ v, Math.abs(i - numberSet.first()) ]); // convert each num into matrix where row is num and column is index of num relative to the first one in set
  let currentIndex = numberSet.first(); // index for first num from list
  const currentNum = distanceMatrix[currentIndex][0];
  const currentDistance = distanceMatrix[currentIndex][1];
  let closestIndex; // index of num which is closer than threshold from current one
  if (currentDistance > threshold) { // if thresh has not been met yet
    for (let i = 1; i <= numberSet.size(); ++i) { // iterate over array, and only between first index and last
      let prevIndex = null;
      while (prevIndex && (distanceMatrix[currentIndex][2] > threshold)) { // while prev index is closer than thresh to curent index
        prevIndex = distanceMatrix.indexOf(prevIndex);
      }
      const numsDistance = Math.abs((i - numberSet.first()) - currentNum) + 1; // distance between i and current num (1 because it's not the same num)
      if (!closestIndex || numsDistance < closestIndex && numsDistance != prevIndex && numsDistance > threshold) { // set new one as index of closest to curent that is closer than thresh from prev index
        closestIndex = i;
      } else if (numsDistance == prevIndex) { // update distance if