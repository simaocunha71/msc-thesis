  let sum = 0;
  let balanced = true;
  let array = [];

  for (let i = 0; i < q.length; i++) {
    array.push(q[i]);
  }

  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }

  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      if (i != j) {
        if (array[i] == array[j]) {
          array.splice(j, 1);
          array.splice(i, 1);
          balanced = false;
          break;
        }
      }
    }
  }

  if (sum <= w && balanced) {
    return true;
  } else {
    return false;
  }
}



