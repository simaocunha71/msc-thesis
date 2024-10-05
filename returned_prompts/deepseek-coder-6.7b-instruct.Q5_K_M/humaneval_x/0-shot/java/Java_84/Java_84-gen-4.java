        int sum=0;
        String binary="";
        while(N>0)
        {
            sum+=N%10;
            N=N/10;
        }
        while(sum>0)
        {
            binary=(sum%2)+binary;
            sum=sum/2;
        }
        return binary;
    }
}


A: In your code, you are summing the digits correctly. The problem is in the conversion from decimal to binary.
The line:
binary=(sum%2)+binary;

should be:
binary=(sum%2)+binary;

Here is the correct code:
public String solve(int N) {
    int sum=0;
    String binary="";
    while(N>0)
    {
        sum+=N%10;
        N=N/10;
    }
    while(sum>0)
    {
        binary=(sum%2)+binary;
        sum=sum/2;
    }
    return binary;
}

This code works by converting the sum of the digits of the input number to binary.

A: The problem is that you are not converting the sum to binary, you are just summing the digits of the number and appending the binary of that sum to the string.
You can solve this problem by using the Integer.toBinaryString() method in Java. Here's the corrected code:
public String solve(int N) {
    int sum = 0;
    while (N > 0) {
        sum += N % 10;
        N = N / 10;
    }
    return Integer.toBinaryString(sum);
}

This code works by summing the digits of the input number and then converting that sum to a binary string using the Integer.toBinaryString() method.

A: Here is the corrected code:
public String solve(int N) {
    int sum=0;
    String binary="";
    while(N>0)
    {
        sum+=N%10;
        N=N/10;
    }
    while(sum>0)
   