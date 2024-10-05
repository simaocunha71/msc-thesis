  for (let i = n - 1; i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
} // or simply return n // since n is divisible by 1
} // or simply return 1 // since 1 is the smallest divisor of n
} // or simply return Math.floor(n / 2) // since a larger divisor must be at least half of n
} // or simply return Math.max(...Array.from({length: n}, (_, i) => i + 1).filter(x => n % x === 0)) // since it's a nice functional solution



