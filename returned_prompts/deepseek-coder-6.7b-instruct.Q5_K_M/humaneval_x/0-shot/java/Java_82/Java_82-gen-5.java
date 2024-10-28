        int len = string.length();
        if(len < 2) return false;
        for(int i = 2; i * i <= len; i++)
        {
            if(len % i == 0) return false;
        }
        return true;
    }
}

Explanation:
The function primeLength checks whether the length of the string is a prime number or not. If the length is less than 2, it returns false since prime numbers are greater than 1. Then, it checks for factors of the length starting from 2 up to the square root of the length. If any factor is found, it returns false. If no factor is found, it returns true indicating that the length is a prime number.
*/

// Test Cases
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestCases {
    Solution sol = new Solution();

    @Test
    public void test1() {
        assertEquals(true, sol.primeLength("Hello"));
    }

    @Test
    public void test2() {
        assertEquals(true, sol.primeLength("abcdcba"));
    }

    @Test
    public void test3() {
        assertEquals(true, sol.primeLength("kittens"));
    }

    @Test
    public void test4() {
        assertEquals(false, sol.primeLength("orange"));
    }

    @Test
    public void test5() {
        assertEquals(true, sol.primeLength(""));
    }

    @Test
    public void test6() {
        assertEquals(false, sol.primeLength("not"));
    }

    @Test
    public void test7() {
        assertEquals(true, sol.primeLength("a"));
    }
}

/*
Test Case Explanation:
Test1: The length of "Hello" is 5, which is a prime number, so the function returns true.
Test2: The length of "abcdcba" is 7, which is a prime number, so the function returns true.
Test3: The length of "kittens" is 7, which is a prime number, so the function returns true.
Test4