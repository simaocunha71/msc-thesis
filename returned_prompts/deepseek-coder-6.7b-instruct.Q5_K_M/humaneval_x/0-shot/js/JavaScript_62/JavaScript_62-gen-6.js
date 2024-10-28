  // If the polynomial has no terms, its derivative is also the empty polynomial.
  if (xs.length === 0) {
    return [];
  }

  // The derivative of a constant is zero, so we can ignore the first term.
  // Then, for each term xs[i] * x^i, we get the derivative as xs[i+1] * x^(i-1)
  // Skipping the first term and adjusting the exponent, we get the result.
  return xs.slice(1).map((x, i) => (i + 1) * x);
};


// Test cases:
console.log(derivative([3, 1, 2, 4, 5])); // [1, 4, 12, 20]
console.log(derivative([1, 2, 3])); // [2, 6]
console.log(derivative([])); // []


```



## Haskell


```Haskell
derivative :: [Integer] -> [Integer]
derivative [] = []
derivative (_:xs) = zipWith (*) (map snd (zip [0..] xs)) (map (*) (map (+1) [0..]) [1..])
```



## J


```J
NB. The derivative of a constant is zero, so we ignore the first term.
NB. For each term xs[i] * x^i, the derivative is xs[i+1] * x^i
derivative=: (1:{~(2#~(+/~1)@(1&{~1{~1#~1)@1))})@.{~(2#~(+/~1)@(1&{~1{~1#~1)@1))}
```



## Julia


```julia
function derivative(xs)
    # If the polynomial has no terms, its derivative is also the empty polynomial.
    if isempty(xs)
        return []
    end

    # The derivative of a constant is zero, so we can ignore the first term