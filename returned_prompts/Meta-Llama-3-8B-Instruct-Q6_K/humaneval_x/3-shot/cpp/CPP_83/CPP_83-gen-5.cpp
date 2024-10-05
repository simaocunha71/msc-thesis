    int count = 0;
    // all numbers that start with 1
    for (int i = 1; i <= 9; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            int num = i * pow(10, j) + (i + 1) * pow(10, n - 1 - j);
            count++;
        }
    }
    // all numbers that end with 1
    for (int i = 1; i <= 9; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            int num = i * pow(10, j) + (i + 1) * pow(10, n - 1 - j);
            count++;
        }
    }
    return count;
} // ends with 1 or starts with 1
int main() {
    int n = 2;
    cout << "Number of n-digit positive integers that start or end with 1: " << starts_one_ends(n) << endl;
    return 0;
}
// The function starts_one_ends() is a counting function. It counts all the n-digit positive integers that start or end with 1. It first calculates all the numbers that start with 1 and then all the numbers that end with 1. It uses a nested loop structure to generate all the n-digit numbers. The outer loop runs from 1 to 9 (for all possible first digits), and the inner loop runs from 0 to n-2 (for all possible digits after the first one). The function then returns the total count. The main function is used to test the starts_one_ends() function. It takes an integer n as input, which is the number of digits for the n-digit positive integers. It then prints the result of the starts_one_ends() function for the given n. In this case, n is 2. The output will be the number of 2-digit positive integers that start or end with 1.