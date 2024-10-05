  let smallest = [Infinity, -1];
  for (let i = 0; i < arr.length; i++) {
      if (arr[i] < smallest[0] && arr[i] % 2 == 0) {
          smallest = [arr[i], i];
      }
  }
  return smallest[1] != -1 ? smallest : [];
}


