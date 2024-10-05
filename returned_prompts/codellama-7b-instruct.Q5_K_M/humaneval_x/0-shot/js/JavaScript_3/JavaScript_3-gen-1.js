  const balance = operations.reduce((acc, curr) => acc + curr, 0);

  if (balance < 0) {
    return true;
  }

  return false;
};

