    double num = stod(value);
    int int_num = int(num);
    if(num - int_num < 0.5)
        return int_num;
    else
        return int_num + 1;
}

int main()
{
    string val = "10";
    cout << closest_integer(val);
    return 0;
}

Output:
10

Explanation:
We use the `stod` function to convert the string value into a double.
Then we convert this double to an integer with the `int` function.
If the difference between the double and the integer is less than 0.5, we return the integer. Otherwise, we return the integer plus one. This ensures that we always round away from zero.
In the example, the double value is 10.0 and the integer is 10. Since the difference is less than 0.5, we return 10. If the value was 10.5, we would return 11, since the difference is greater than 0.5.