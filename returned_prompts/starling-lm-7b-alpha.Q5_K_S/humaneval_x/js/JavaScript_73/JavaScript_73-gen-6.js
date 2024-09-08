  const odd_index_value = arr[Math.floor(arr.length / 2)];
  const even_index_value = arr[arr.length - 1];

  const odd_count = (arr.length + 1) / 2;
  const even_count = arr.length - odd_count;

  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    if (i < odd_count && arr[i] != odd_index_value) {
      count += 1;
    } else if (i >= odd_count && arr[i] != even_index_value) {
      count += 1;
    }
  }

  return count;
}



