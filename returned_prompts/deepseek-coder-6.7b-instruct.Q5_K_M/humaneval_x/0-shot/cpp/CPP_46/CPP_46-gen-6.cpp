  int i;
  int f1 = 0, f2 = 0, f3 = 2, f4 = 0, fn = 0;

B:
  if(n == 0){
    return f1;
  }
  else if(n == 1){
    return f2;
  }
  else if(n == 2){
    return f3;
  }
  else if(n == 3){
    return f4;
  }

C:
  for(i = 4; i <= n; i++){
    fn = f1 + f2 + f3 + f4;
    f1 = f2;
    f2 = f3;
    f3 = f4;
    f4 = fn;
  }

D:
  return fn;
}

int main(){
  printf("%d\n", fib4(5));
  printf("%d\n", fib4(6));
  printf("%d\n", fib4(7));
  return 0;
}

Answer:
The function fib4(int n) is a function that computes the n-th element of a custom number sequence.
The function uses a loop that starts from 4 and continues until n. Inside the loop, the function computes the next number of the sequence by adding the previous 4 numbers. The previous 4 numbers are stored in f1, f2, f3 and f4 and are updated in each iteration of the loop. 
At the end of the loop, the function returns fn, which is the n-th number of the sequence.
The main function calls fib4 with different values of n and prints the result.
The time complexity of this function is O(n) as it loops from 4 to n. The space complexity is O(1) as it uses a constant amount of space to store the 4 initial numbers of the sequence and the current number.
The function is efficient because it does not use recursion and instead uses a loop to compute the sequence.
*/

// end answer

