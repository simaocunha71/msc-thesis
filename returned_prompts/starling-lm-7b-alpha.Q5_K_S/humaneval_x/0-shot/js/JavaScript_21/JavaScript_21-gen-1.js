  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const range = max - min;

  return numbers.map(number => {
    return (number - min) / range;
  });

};







/*
  >>> rescaleToUnit(100)
  [0, 1]
  >>> rescaleToUnit(2)
  [0, 1]
  >>> rescaleToUnit(1)
  [0]
  >>> rescaleToUnit(0)
  []
  >>> rescaleToUnit([-1, 1])
  [-1, 1]
  >>> rescaleToUnit([])
  []
  >>> rescaleToUnit([1, 2, 3, 4, 5])
  [0, 0.2, 0.4, 0.6, 1]
  >>> rescaleToUnit([-1, 0, 1])
  [-1, 0, 1]
  >>> rescaleToUnit(2)
  [0, 1]
  >>> rescaleToUnit([-1, 1])
  [-1, 1]
  >>> rescaleToUnit(0)
  []
  >>> rescaleToUnit([0, 0, 0, 0, 0])
  [0]
  >>> rescaleToUnit(100)
  [0, 1]
  >>> rescaleToUnit([100, 200, 300, 400, 500])
  [0, 0.5, 1, 1.5, 2]
  >>> rescaleToUnit([-10, -5, 0, 5, 10])
  [-1, -0.5, 0, 0.5, 1]
  >>> rescaleToUnit([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
  [0, 0.1, 0.2, 0.3, 