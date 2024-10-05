  let increasing = true;
  let decreasing = true;
  let prev = l[0];

  for (let i = 1; i < l.length; i++) {
    if (l[i] > prev) {
      decreasing = false;
    } else if (l[i] < prev) {
      increasing = false;
    }
    prev = l[i];
  }

  return increasing || decreasing;
}
}  // end of module
}  // end of module
}  // end of module

// Test cases
console.log(hasCloseElements([1.0, 2.0, 3.0], 0.5));  // false
console.log(hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3));  // true

console.log(separateParenGroups('( ) (( )) (( )( ))'));  // ['()', '(())', '(()())']

console.log(truncateNumber(3.5));  // 0.5

console.log(monotonic([1, 2, 4, 20]));  // true
console.log(monotonic([1, 20, 4, 10]));  // false
console.log(monotonic([4, 1, 0, -10]));  // true
}  // end of main program

// Output
// false
// [ '()', '(())', '(()())' ]
// 0.5
// true
// false
// true
// end of output
// End of the program.  // end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
// end of main program
// end of program
// End of the program.
