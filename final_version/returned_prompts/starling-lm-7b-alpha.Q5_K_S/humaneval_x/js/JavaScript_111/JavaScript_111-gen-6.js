  const input_string = test;
  let result = {};
  for (const c of input_string) {
    if (result[c] === undefined) {
      result[c] = 0;
    }
    result[c] += 1;
  }

  const result_array = Object.entries(result).map(
    ([key, value]) => [key, value]
  );
  result_array.sort((a, b) => b[1] - a[1]);

  if (result_array.length == 1) {
    return result_array[0];
  } else {
    return result_array.map(([key, value]) => {
      return {
        [key]: value
      }
    });
  }
}



