/* Check if in given list of numbers, are any two numbers closer to each other than
  given threshold.
  >>> hasCloseElements([1.0, 2.0, 3.0], 0.5)
  false
  >>> hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
  true
  */
const hasCloseElements = (numbers, threshold) => {
  const distances = numbers.map((n) => Math.abs(n));
  
  // sort the list of numbers, so we can compare and check
  distances.sort();
  let minDistance = Infinity;
  
  for (let i = 0; i < distances.length - 1; ++i) {
    const indexOfCurrent = i;
    
    // if last element is closer to current than the threshold, then there's a match
    while(indexOfCurrent + 1 < distances.length && Math.abs((distances[indexOfCurrent] + distances[indexOfCurrent + 1]) / 2) < threshold) {
      indexOfCurrent++; // next index position is one ahead of current
    }
    
    if (indexOfCurrent > -1 && indexOfCurrent + 1 > -1) {
      minDistance = Math.min(distances[indexOfCurrent], distances[indexOfCurrent + 1]);
      
      // if element at lower index is closer to the current than threshold, then there's a match
      while ((indexOfCurrent - 1) >= 0 && Math.abs((distances[indexOfCurrent] + distances[indexOfCurrent + 1]) / 2) < threshold) {
        minDistance = Math.min(distances[indexOfCurrent], distances[indexOfCurrent + 1]);
        
        if (indexOfCurrent !== 0 && indexOfCurrent - 1 > -1) { // otherwise continue on lower element
          indicesDiff--;
          
          // don't go back to the beginning, that would make us start over
          for (let i = 0; i < distances.length - 1 && indicesDiff >= 0 ; ++i) { // if we have not yet found a match for this element
            index