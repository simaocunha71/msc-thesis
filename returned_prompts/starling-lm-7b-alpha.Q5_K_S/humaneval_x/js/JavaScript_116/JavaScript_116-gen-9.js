  const binary_count = arr.map(num => {
    let binary = (num >>> 0).toString(2);
    return binary.length - binary.match(/[1]/g).length;
  });

  const decimal_count = arr.map(num => {
    return num;
  });

  return [...arr].sort((a, b) => {
    let compare_binary = binary_count[a] - binary_count[b];
    if (compare_binary != 0) {
      return compare_binary;
    } else {
      return decimal_count[a] - decimal_count[b];
    }
  });
};



