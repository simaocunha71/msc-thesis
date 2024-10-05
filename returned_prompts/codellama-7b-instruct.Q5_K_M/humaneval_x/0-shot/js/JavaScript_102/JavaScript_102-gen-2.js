/*
  This is a very interesting problem. The first thing that came to my mind
  was to find the closest even number to x and y. But that won't work because
  if we have x=13 and y=15 then we need to find the closest even number to
  13 and 15.

  The second idea was to find the greatest even number smaller than x or y
  (if they're even) and then check if that number is in the range [x, y].
  That works but it's not the most efficient solution.

  After some thought I came up with this solution:

  The idea is to find the greatest even number smaller than x and then check
  if that number is in the range [x, y]. If that's the case then we return
  that number. If not, then we need to find the greatest even number smaller
  than y and check if that number is in the range [x, y].

  The function works because if x and y are in the range [x, y] then there's
  always an even number smaller than x or y that's in the range [x, y].
*/
const chooseNum = (x, y) => {
  let closestEvenNumber = Math.floor(x / 2) * 2
  if (closestEvenNumber >= x && closestEvenNumber <= y) {
    return closestEvenNumber
  }
  closestEvenNumber = Math.floor(y / 2) * 2
  if (closestEvenNumber >= x && closestEvenNumber <= y) {
    return closestEvenNumber
  }
  return -1
}

