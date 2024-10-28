        int largest = -1;

        while (n % 2 == 0) {
            largest = 2;
            n >>= 1;
        }

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largest = i;
                n = n / i;
            }
        }

        if (n > 2)
            largest = n;

        return largest;
    }
}

The algorithm works by dividing the input number by 2 as long as it's possible, then it continues with the odd numbers, dividing by them as long as possible. The largest number that the number could be divided by is the largest prime factor.

The reason why we only need to check up to sqrt(n) is because a larger factor of n must be a multiple of a smaller factor that has already been checked.

The reason why we start from 3 and increment by 2 each time is because even numbers aren't prime, so we don't need to check them.

The reason why we check up to sqrt(n) and not n is because a larger factor of n must be a multiple of a smaller factor that has already been checked.

The reason why we check if n > 2 after the loop is because if n is still greater than 2 at the end, it means that it's the largest prime factor.

The reason why we return largest at the end is because that's the largest prime factor we found.

The reason why we use >>= 1 instead of /= 2 is because it's more efficient to use a bitwise shift operation than to use the division operation.

The reason why we use n =