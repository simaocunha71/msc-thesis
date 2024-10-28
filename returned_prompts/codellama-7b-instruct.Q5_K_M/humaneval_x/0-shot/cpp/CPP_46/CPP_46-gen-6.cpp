  return 0;
}

// Fib4(n) = Fib4(n-1) + Fib4(n-2) + Fib4(n-3) + Fib4(n-4)
// Fib4(n-4) = Fib4(n-5) + Fib4(n-6) + Fib4(n-7) + Fib4(n-8)
// Fib4(n-8) = Fib4(n-9) + Fib4(n-10) + Fib4(n-11) + Fib4(n-12)
// Fib4(n-12) = Fib4(n-13) + Fib4(n-14) + Fib4(n-15) + Fib4(n-16)
// ...
// Fib4(n-4) = Fib4(n-5) + Fib4(n-6) + Fib4(n-7) + Fib4(n-8)
// Fib4(n-3) = Fib4(n-4) + Fib4(n-5) + Fib4(n-6) + Fib4(n-7)
// Fib4(n-2) = Fib4(n-3) + Fib4(n-4) + Fib4(n-5) + Fib4(n-6)
// Fib4(n-1) = Fib4(n-2) + Fib4(n-3) + Fib4(n-4) + Fib4(n-5)
// Fib4(n) = Fib4(n-1) + Fib4(n-2) + Fib4(n-3) + Fib4(n-4)

// Fib4(0) -> 0
// Fib4(1) -> 0
// Fib4(2) -> 2
// Fib4(3) -> 0

// Fib4(4) = Fib4(4-1) + Fib4(4-2) + Fib4(4-3) + F