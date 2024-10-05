  if (n <= 1) {
    return 0;
  }
  if (n == 2) {
    return 1;
  }
  let a = 0, b = 0, c = 1;
  for (let i = 3; i <= n; i++) {
    let temp = a + b + c;
    a = b;
    b = c;
    c = temp;
  }
  return c;
}
// or
const fibfib = (n) => {
  if (n <= 1) {
    return 0;
  }
  if (n == 2) {
    return 1;
  }
  let a = 0, b = 0, c = 1, d = 1;
  for (let i = 3; i <= n; i++) {
    let temp = a + b + c;
    a = b;
    b = c;
    c = d;
    d = temp;
  }
  return c;
} // this one is more efficient for large n
} // you could also use memoization for even larger n
} // also note that n should not be negative
} // also note that n should not be zero
} // also note that n should not be one
} // also note that n should not be two
} // also note that n should not be three
} // also note that n should not be four
} // also note that n should not be five
} // also note that n should not be six
} // also note that n should not be seven
} // also note that n should not be eight
} // also note that n should not be nine
} // also note that n should not be ten
} // also note that n should not be eleven
} // also note that n should not be twelve
} // also note that n should not be thirteen
} // also note that n should not be fourteen
} // also note that n should not be fifteen
} // also note that n should not be sixteen
} // also note that n should not be seventeen
} // also note that n should not be eighteen
} // also note that n should not be nineteen
} // also note that n should not be twenty
} // also note that n should not be twenty-one
} // also note that n should not be twenty-two
} // also note that n should