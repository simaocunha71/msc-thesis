  return xs.map((x, i, xs) => i < 1 ? 0 : xs[i - 1] * i)
}

/*
