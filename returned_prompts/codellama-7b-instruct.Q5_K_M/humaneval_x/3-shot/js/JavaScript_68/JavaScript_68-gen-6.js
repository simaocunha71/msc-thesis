  const find_smallest = (arr) => {
    const even_arr = arr.filter(n => n % 2 === 0);
    if (even_arr.length == 0) {
      return [null, null];
    }
    return even_arr.reduce((acc, cur, i, arr) => {
      if (cur < acc[0]) {
        return [cur, i];
      }
      return acc;
    }, [Number.POSITIVE_INFINITY, 0]);
  }
  const [smallest_value, smallest_index] = find_smallest(arr);
  if (smallest_value === null) {
    return [];
  }
  const smallest_node = arr.splice(smallest_index, 1)[0];
  return [smallest_node, smallest_index];
}



