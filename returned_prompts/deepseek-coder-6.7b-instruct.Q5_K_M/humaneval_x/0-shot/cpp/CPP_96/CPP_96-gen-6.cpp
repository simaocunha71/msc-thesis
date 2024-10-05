  vector<int> primes;

  if (n < 2) return primes;

  primes.push_back(2);
  for (int i = 3; i < n; i += 2) {
    bool isPrime = true;
    for (int j = 0; j < primes.size(); j++) {
      if (i % primes[j] == 0) {
        isPrime = false;
        break;
      }
      if (primes[j] * primes[j] > i) break;
    }
    if (isPrime) primes.push_back(i);
  }
  return primes;
}

int main(){
  int n;
  printf("Enter a number: ");
  scanf("%d",&n);
  vector<int> primes = count_up_to(n);
  printf("Prime numbers: ");
  for (int i = 0; i < primes.size(); i++) printf("%d ", primes[i]);
  printf("\n");
  return 0;
}
```

This C++ code works by iteratively checking each number to see if it is prime. If it is, it is added to the vector. The prime checking is done by iterating over the existing primes and checking if the number can be divided evenly by any of them. If not, it is prime.

This code could be optimized by only checking divisibility up to the square root of the number and by skipping even numbers after 2.

Also, note that this code returns an empty vector for input numbers less than 2 as there are no prime numbers in that range.

Please note that this code does not handle large numbers well due to the nature of prime checking.

Also, it's not a good practice to use the `using namespace std;` in a larger code as it can cause naming conflicts.

Hope this helps.
*/

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    vector<int> primes = count_up_to(n);
    printf("Prime numbers: ");
    for (int i = 0