  let min_changes = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] == arr[j]) {
        continue;
      }
      let changes = 0;

      for (let k = i; k < j; k++) {
        if (arr[k] == arr[j]) {
          changes++;
          break;
        }
        if (arr[k] == arr[i]) {
          changes++;
        }
      }

      min_changes = Math.min(min_changes, changes);
    }
  }

  return min_changes;
}



