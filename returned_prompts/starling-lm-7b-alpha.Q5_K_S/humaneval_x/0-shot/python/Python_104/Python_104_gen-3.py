    def unique_digits(x):
        def has_even(n):
            while n:
                if n % 2 == 0:
                    return True
                n //= 10
            return False

        return sorted([i for i in x if not has_even(i)])

    return unique_digits(x)


# Here is a Python3 implementation of the above algorithm.
def unique_digits(x):
    def has_even(n):
        while n:
            if n % 2 == 0:
                return True
            n = n // 10
        return False

    return sorted([i for i in x if not has_even(i)])


# Here is a Python2 implementation of the above algorithm.
def unique_digits(x):
    def has_even(n):
        while n:
            if n % 2 == 0:
                return True
            n /= 10
        return False

    return sorted([i for i in x if not has_even(i)])


# Here is a C++ implementation of the above algorithm.
#include <algorithm>
#include <iostream>
#include <vector>

std::vector<int> unique_digits(std::vector<int> x) {
    std::function<bool(int)> has_even = [](int n) {
        while (n) {
            if (n % 2 == 0) {
                return true;
            }
            n /= 10;
        }
        return false;
    };

    std::vector<int> result;
    std::copy_if(x.begin(), x.end(), std::back_inserter(result),
                 [&](int n) { return !has_even(n); });
    std::sort(result.begin(), result.end());
    return result;
}


# Here is a Java implementation of the above algorithm.
import java.util.Arrays;
import java.util.function.Predicate;

public class UniqueDigits {
    private static Predicate<Integer> has_even