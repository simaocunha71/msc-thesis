  const minMax = (lst) => {
    let min = lst[0];
    let max = lst[0];
    const indexes = [];

    for (let i = 1; i < lst.length; i++) {
      indexes.push(i);
      if (lst[i] < min) min = lst[i];
      if (lst[i] > max) max = lst[i];
    }

    return { min, max, indexes };
  };

  const sort = (lst) => {
    const { min, max, indexes } = minMax(lst);
    const result = [];

    for (const index of indexes) {
      result.push(lst[index]);
    }

    result.push(min);
    result.push(max);

    return result;
  };

  return sort(lst);
}



