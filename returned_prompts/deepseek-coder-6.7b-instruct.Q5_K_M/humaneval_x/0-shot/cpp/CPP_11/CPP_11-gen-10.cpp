    string xor_res = "";
    for (int i=0; i<a.length(); i++)
    {
        if (a[i] == b[i])
            xor_res += '0';
        else
            xor_res += '1';
    }
    return xor_res;
}

int main()
{
    string a, b;
    scanf("%s %s", &a, &b);
    printf("%s", string_xor(a, b).c_str());
    return 0;
}

Explanation:
We are given two binary strings a and b of same length. We have to perform a binary XOR operation on these two strings and return result as a string.
In binary XOR, 1 XOR 1 or 0 XOR 0 gives 0 and 1 XOR 0 or 0 XOR 1 gives 1.
So we iterate over each character in the strings and compare them. If they are same, we add 0 to our result string, else we add 1 to our result string. After the loop ends, we return our result string.
*/

int main() {
    string a, b;
    cin >> a >> b;
    cout << string_xor(a, b);
    return 0;
}

Explanation:
We are given two binary strings a and b of same length. We have to perform a binary XOR operation on these two strings and return result as a string.
In binary XOR, 1 XOR 1 or 0 XOR 0 gives 0 and 1 XOR 0 or 0 XOR 1 gives 1.
So we iterate over each character in the strings and compare them. If they are same, we add 0 to our result string, else we add 1 to our result string. After the loop ends, we return our result string.
*/

int main() {
    string a, b;
    cin >> a >> b;
    cout << string_xor(a, b);
    return 0;
}

Explanation:
We are given two binary strings a and b of same length. We have to perform a binary XOR operation on