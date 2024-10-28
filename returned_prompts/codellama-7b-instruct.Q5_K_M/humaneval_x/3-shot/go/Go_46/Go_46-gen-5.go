    if n <= 0 { return 0 }
    if n == 1 { return 0 }
    if n == 2 { return 2 }
    if n == 3 { return 0 }

    var nMinus1, nMinus2, nMinus3, nMinus4 int = Fib4(n-1), Fib4(n-2), Fib4(n-3), Fib4(n-4)
    return nMinus1 + nMinus2 + nMinus3 + nMinus4
}



