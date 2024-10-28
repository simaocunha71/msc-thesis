  if (arr.length == 0) {
    return [];
  }
  const even_values = arr.filter((node) => node % 2 == 0);
  if (even_values.length == 0) {
    return [];
  }
  const smallest_even_value = even_values.reduce((acc, node) => Math.min(acc, node));
  const smallest_even_node_index = arr.indexOf(smallest_even_value);
  return [smallest_even_value, smallest_even_node_index];
}



