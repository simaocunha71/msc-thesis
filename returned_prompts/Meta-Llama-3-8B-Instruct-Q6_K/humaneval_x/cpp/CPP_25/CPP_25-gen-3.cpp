    vector<int> factors;
    for(int i = 2; i <= n; i++){
        int count = 0;
        while(n % i == 0){
            n /= i;
            count++;
        }
        if(count > 0){
            factors.push_back(i);
            factors.insert(factors.end(), count, i);
        }
    }
    return factors;
}

int main()
{
    int num;
    printf("Enter a number: ");
    scanf("%d",&num);
    vector<int> result = factorize(num);
    printf("Prime factors: ");
    for(int i = 0; i < result.size(); i++)
        printf("%d ", result[i]);
    printf("\n");
    return 0;
}  // Time complexity O(sqrt(n))


Solution:
The problem is to find the prime factors of a given integer and return them as a vector in the order from smallest to largest. Each factor should be included in the vector the number of times it appears in the factorization.

Here is a simple and efficient solution using a vector in C++:

```cpp
#include <vector>
#include <algorithm>

std::vector<int> factorize(int n) {
    std::vector<int> factors;
    for (int i = 2; i <= n; i++) {
        int count = 0;
        while (n % i == 0) {
            n /= i;
            count++;
        }
        if (count > 0) {
            factors.push_back(i);
            factors.insert(factors.end(), count, i);
        }
    }
    return factors;
}
```

This function works by iterating from 2 to the given number `n`, and for each number `i` in this range, it checks how many times `i` divides `n`. If `i` divides `n`, it divides `n` by `i` and increments the count. If the count is greater than 0, it adds `i` to the vector `factors` and inserts `i` into the vector `count` times.

Here is the main function to test the `factorize` function:

```cpp
int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    std::vector<int> result = factorize(num);
    printf("Prime factors: ");
    for (int i = 0; i < result.size(); i++)
        printf("%d ", result[i]);
   