    string str = to_string(N);
    int sum = 0;
    for(int i = 0; i < str.length(); i++){
        sum += (str[i] - '0');
    }
    return to_string(sum);
}

int main() {
    int N;
    cin >> N;
    string res = solve(N);
    cout << res;
    return 0;
}

Explanation:
The task is to find the total sum of the digits of a given number in binary form. The given number is initially converted to a string. Then, a loop is used to iterate through each character in the string. The ASCII value of each character is subtracted by the ASCII value of '0' to get the actual digit value. The sum of these digit values is calculated. Finally, the sum is converted back to a string and returned as the output.
*/



