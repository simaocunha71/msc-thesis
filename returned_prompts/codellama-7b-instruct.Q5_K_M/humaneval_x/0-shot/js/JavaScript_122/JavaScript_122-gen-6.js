
    return arr
      .slice(0, k)
      .reduce((acc, el) => acc + el, 0);

  };

  const test = arr => addElements(arr, 4);

  const test1 = () => {
    const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
    return [4];
  };

  const test2 = () => {
    const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
    return [24];
  };

  const test3 = () => {
    const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
    return [9];
  };

  const test4 = () => {
    const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
    return [10];
  };

  const test5 = () => {
    const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
    return [20];
  };

  const test6 = () => {
    const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
    return [18];
  };

  const test7 = () => {
    const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
    return [16];
  };

  const test8 = () => {
    const arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];
    return [14];
  };