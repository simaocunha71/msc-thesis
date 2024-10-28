  return numbers.reduce((acc, current, index) => {
    if (index > 0) {
      acc.push(delimeter);
    }
    acc.push(current);
    return acc;
  }, []);
}