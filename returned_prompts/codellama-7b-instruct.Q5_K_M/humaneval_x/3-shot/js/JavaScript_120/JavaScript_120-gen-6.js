  var heap = [];

  for (let i = 0; i < k; i++) {
    heap.push(arr[i]);
  }

  for (let i = k; i < arr.length; i++) {
    if (arr[i] > heap[0]) {
      heap.shift();
      heap.push(arr[i]);
    }
  }

  return heap.sort((a, b) => b - a);
}



