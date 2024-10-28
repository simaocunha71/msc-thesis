

/*
I know that the fib4 sequence is similar to the fibbonacci sequence but with the difference that there are 4 numbers that make up the fib4 sequence.
So I started by creating a function that takes in a number and returns the n-1 number of the sequence.
I then created another function that takes in the n-2 number of the sequence and returns the n-3 number.
I then created another function that takes in the n-3 number of the sequence and returns the n-4 number.
I then created a function that takes in the n-1 number of the sequence and returns the n-4 number plus the n-3 number plus the n-2 number plus the n-1 number.
I then created the main function that takes in the number and then calls all the other functions.
*/

const fib4 = (n) => {
  const fib4_n_minus_1 = (n_minus_1) => {
    if (n_minus_1 == 0) return 0;
    return fib4_n_minus_2(n_minus_1 - 1) + fib4_n_minus_3(n_minus_1 - 1) + fib4_n_minus_4(n_minus_1 - 1) + fib4_n_minus_1(n_minus_1 - 1);
  };
  const fib4_n_minus_2 = (n_minus_2) => {
    if (n_minus_2 == 0) return 0;
    return fib4_n_minus_3(n_minus_2 - 1) + fib4_n_minus_4(n_minus_2 - 1) + fib4_n_minus_1(n_minus_2 - 1);
  };
  const fib4_n_minus_3 = (n_minus_3) => {
    if (n_minus_3 == 0) return 0;
    return fib4_n_minus_4(n_minus_3 - 1) + fib4_n_minus_1(n_minus_3 - 1);
  };
  const fib4_n_minus_4 = (n_minus_4) => {
    if (