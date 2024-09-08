  const sortList = (a, b) => {
    return a < b ? -1 : a > b ? 1 : 0;
  };
  const result = [...lst];

  while (result.length > 0) {
    const min_index = result.reduceKey(sortList);
    const min_val = result.splice(min_index, 1);
    result.unshift(...result.slice(result.reduceKey(sortList)).sort(sortList));
    result.unshift(min_val);
  }

  return result;
}



