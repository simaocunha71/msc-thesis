        return number - (int)number;

    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.truncateNumber(3.5));
    }
}

This program takes a double number as an input, and returns the decimal part of that number. It does this by subtracting the integer part of the number from the original number. The integer part of the number is obtained by casting the number to an int, which effectively truncates the decimal part. The result is the decimal part of the original number.

The time complexity of this solution is O(1), which means it always takes the same amount of time to execute, regardless of the input size. The space complexity is also O(1), as it only uses a constant amount of space to store the input and the result.

Note: This solution assumes that the input is always a positive floating point number. If the input could be negative, the solution would need to be modified to handle this case correctly.
    """
    return number - (int)number

def main():
    s = Solution()
    print(s.truncateNumber(3.5))

if __name__ == "__main__":
    main()

# Output: 0.5

This program works in a similar way to the previous one, but uses a function instead of a method. The main difference is that it uses a class-based approach to solve the problem, while the previous solution used a functional approach. This approach is more common in languages like Java, but it can also be used in Python.
    """
    return number - (int)number

def main():
    s = Solution()
    print(s.truncateNumber(3.5))

if __name__ == "__main__":
    main()

# Output: 0.5
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3: Given an array of integers, write a program to find the sum of the largest and smallest integers in the array.
<jupyter_code>
