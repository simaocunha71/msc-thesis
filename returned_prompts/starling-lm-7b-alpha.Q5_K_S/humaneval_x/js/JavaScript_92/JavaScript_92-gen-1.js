  return (
    (x == y + z && typeof(x) == 'number' && typeof(y) == 'number' && typeof(z) == 'number' && typeof(y + z) == 'number') ||
    (y == x + z && typeof(x) == 'number' && typeof(y) == 'number' && typeof(z) == 'number' && typeof(x + z) == 'number') ||
    (z == x + y && typeof(x) == 'number' && typeof(y) == 'number' && typeof(z) == 'number' && typeof(x + y) == 'number')
  );
}



