    string binary = "";
    while(decimal > 0){
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal = decimal / 2;
    }
    return "db" + binary + "db";
}

int main() {
    printf("%s\n", decimal_to_binary(15));
    printf("%s\n", decimal_to_binary(32));
    return 0;
}

Output:
db1111db
db100000db

Explanation:
In this problem, we are given a decimal number and we need to convert it into binary. We can achieve this by using a while loop. In each iteration of the loop, we divide the decimal number by 2 and append the remainder (0 or 1) to the beginning of the binary string. We do this until the decimal number becomes 0. Finally, we append "db" to the beginning and end of the binary string. The "db" is used to maintain the correct format.

In the main function, we test our function with decimal numbers 15 and 32 and print the results. The output is as expected, "db1111db" for 15 and "db100000db" for 32. This shows that our function is working correctly.