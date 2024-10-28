import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return true if a given number is prime, and false otherwise.
    >>> isPrime(6)
    false
    >>> isPrime(101)
    true
    >>> isPrime(11)
    true
    >>> isPrime(13441)
    true
    >>> isPrime(61)
    true
    >>> isPrime(4)
    false
    >>> isPrime(1)
    false
     */
    public boolean isPrime(int n) {

    if (n < 2) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
\end{code}

}

Comment: You are not following the instructions. The first example is using `isPrime(101)` and the second example is using `isPrime(13441)` as inputs.  Your code only works for numbers between 2 and 100.

Comment: @Code-Apprentice How can I change this?

Comment: @Code-Apprentice I'm not sure what you mean, I'm just trying to get my code to run to see if it works. The code is supposed to be able to handle any input, and I'm not sure why it's not working.

Comment: You need to add more code to make your current code work. If you don't understand why, you should ask a question about that.

Comment: @Code-Apprentice I'm not sure what you mean by that. I'm not sure what code I need to add to get it to work.

Comment: I'm not sure either. You need to give more details about the problem you are trying to solve.

Comment: @Code-Apprentice I'm just trying to get my code to work with any input, and I'm not sure why it's not working.

Comment: @Code-Apprentice I'm just trying to get my code to run