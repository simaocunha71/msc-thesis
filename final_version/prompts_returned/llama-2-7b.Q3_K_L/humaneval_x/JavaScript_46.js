/*The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
  fib4(0) -> 0
  fib4(1) -> 0
  fib4(2) -> 2
  fib4(3) -> 0
  fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
  Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
  >>> fib4(5)
  4
  >>> fib4(6)
  8
  >>> fib4(7)
  14
  */
const fib4 = (n) => {
    let acc = 0;
    for (let i = n - 2; i >= 0; i--){
        acc += Fib.fib4(i + 1);
    }
    return acc;
}

const Fib = {
    fib: function (n) {
       if (!this.counter) this.counter++;
       else this.counter -= 1
        // this.counter += 1;
        
    if (this.counter === n){
        console.log(this.fib4);
    }
    return this.fib4;
}
};