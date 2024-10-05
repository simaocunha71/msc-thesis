  var result = [];
  var max_so_far = numbers[0];

  for (const n of numbers) {
    if (n > max_so_far) {
      max_so_far = n;
    }
    result.push(max_so_far);
  }

  return result;
}



