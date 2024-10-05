  int i = 0;
  int j = 1;
  int k = 0;
  int count = 0;
  if(n==1)
    return 2;
  if(n==2)
    return 3;
  if(n==3)
    return 5;
  while(count<n){
    int temp = i + j;
    i = j;
    j = temp;
    if(is_prime(temp)){
      count++;
      if(count==n)
        return temp;
    }
  }
}

bool is_prime(int num){
  if(num<=1)
    return false;
  if(num%2==0&&num>2)
    return false;
  for(int i = 3; i * i <= num; i += 2){
    if(num % i == 0)
      return false;
  }
  return true;
}

int main()
{
  int n;
  scanf("%d",&n);
  printf("%d",prime_fib(n));
  return 0;
}

The function is_prime() checks whether a number is prime or not. The function prime_fib() generates Fibonacci series and checks if the number is prime or not, it also counts how many prime numbers have been encountered till now. When the count becomes equal to the input number n, it returns the n-th prime Fibonacci number.

The time complexity of this code is O(n^2) where n is the input number because we are running the is_prime() function in the while loop which runs n times.

The space complexity of this code is O(1) because we are using a constant amount of space to store variables.
*/




































































































