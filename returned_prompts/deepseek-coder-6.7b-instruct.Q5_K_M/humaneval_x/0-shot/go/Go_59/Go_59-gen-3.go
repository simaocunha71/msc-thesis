
// 1. Initialize max_prime as the smallest prime number.
    max_prime := 2

B:

// 2. Divide n by 2 until n becomes odd.
    for n % 2 == 0 {
        n = n / 2
    }

C:

// 3. Now n must be odd. So, start a loop from i = 3 and go upto square root of n.
    for i := 3; i * i <= n; i = i + 2 {

D:

//