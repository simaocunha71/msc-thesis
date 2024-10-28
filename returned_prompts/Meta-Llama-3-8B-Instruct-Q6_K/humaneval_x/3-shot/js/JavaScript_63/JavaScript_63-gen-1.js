  if (n <= 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  } else {
    let a = 0, b = 0, c = 1;
    for (let i = 3; i <= n; i++) {
      let temp = a + b + c;
      a = b;
      b = c;
      c = temp;
    }
    return c;
  }
}
  // Using memoization
  // const memo = {0: 0, 1: 0, 2: 1};
  // return fibfibHelper(n, memo);

  // helper function
  // function fibfibHelper(n, memo) {
  //   if (n <= 1) {
  //     return 0;
  //   } else if (memo[n]) {
  //     return memo[n];
  //   } else {
  //     memo[n] = fibfibHelper(n-1, memo) + fibfibHelper(n-2, memo) + fibfibHelper(n-3, memo);
  //     return memo[n];
  //   }
  // }
}  // End of function fibfib
//  return fibfibHelper(n, memo);
// } // End of function fibfib
//   memo = {0: 0, 1: 0, 2: 1};
// } // End of function fibfib
//   return memo[n];
// } // End of function fibfib
// } // End of function fibfib
//   return memo[n];
// } // End of function fibfib
// } // End of function fibfib
//   memo[n] = fibfibHelper(n-1, memo) + fibfibHelper(n-2, memo) + fibfibHelper(n-3, memo);
//   return memo[n];
// } // End of function fibfib
// } // End of function fibfib
//   memo[n] = fibfibHelper(n-1, memo) + fibfibHelper(n-2, memo) + fibfibHelper(n-3, memo);
//   return memo[n];
// } // End of function fibfib
// } // End of function fibfib
//   memo[n] = fibfibHelper(n-1, memo) + fibfibHelper(n-2, memo) + fibfibHelper(n-3, memo);
//   return memo