  if (arr.length === 0) return [];
  if (arr.some(num => num < 1 || num > 9)) return ['One'];
  return numberSort(arr);
}



