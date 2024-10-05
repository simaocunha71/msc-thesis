    int n = str.length();
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int i = 3; i * i <= n; i += 2)
        if (n % i == 0)
            return false;
    return true;
}

int main()
{
    string str;
    printf("Enter a string: ");
    getline(cin, str);
    if (prime_length(str))
        printf("true\n");
    else
        printf("false\n");
    return 0;
}
*/

int main()
{
    printf("%d\n", prime_length("Hello"));
    printf("%d\n", prime_length("abcdcba"));
    printf("%d\n", prime_length("kittens"));
    printf("%d\n", prime_length("orange"));
    return 0;
}
*/

*/

