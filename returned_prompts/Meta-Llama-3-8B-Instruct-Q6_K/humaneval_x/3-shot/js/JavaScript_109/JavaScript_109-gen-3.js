  if (arr.length === 0) {
    return true;
  }

  let maxIndex = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[maxIndex]) {
      maxIndex = i;
    }
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[(i + maxIndex) % arr.length]) {
      return false;
    }
  }

  return true;
}
// moveOneBall([3, 4, 5, 1, 2]) returns true
// moveOneBall([3, 5, 4, 1, 2]) returns false
// moveOneBall([1, 2, 3, 4, 5]) returns true
// moveOneBall([5, 4, 3, 2, 1]) returns false
// moveOneBall([]) returns true
// moveOneBall([1]) returns true
// moveOneBall([1, 2]) returns true
// moveOneBall([1, 2, 3]) returns true
// moveOneBall([3, 2, 1]) returns false
// moveOneBall([4, 3, 2, 1]) returns false
// moveOneBall([5, 4, 3, 2, 1]) returns false
// moveOneBall([5, 4, 3, 1, 2]) returns false
// moveOneBall([5, 4, 3, 2]) returns false
// moveOneBall([5, 4, 3, 2, 1, 0]) returns false
// moveOneBall([5, 4, 3, 2, 1, 0, 0]) returns false
// moveOneBall([5, 4, 3, 2, 1, 0, 0, 0]) returns false
// moveOneBall([5, 4, 3, 2, 1, 0, 0, 0, 0]) returns false
// moveOneBall([5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) returns false
// moveOneBall([5, 4, 