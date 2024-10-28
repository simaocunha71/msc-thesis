    int sum=0, rem;
    string binary="";
    while(N > 0){
        rem = N % 10;
        sum += rem;
        N = N / 10;
    }
    while(sum > 0){
        rem = sum % 2;
        binary = to_string(rem) + binary;
        sum = sum / 2;
    }
    return binary;
}

int main(){
    int N;
    scanf("%d", &N);
    printf("%s\n", solve(N).c_str());
    return 0;
}

I:
1000
1100
1100

O:
1
110
1100

*/

//src/main/resources/c/digits_sum_in_binary/Solution.java
package digits_sum_in_binary;

public class Solution {
    public static String solve(int N) {
        int sum = 0, rem;
        String binary = "";
        while (N > 0) {
            rem = N % 10;
            sum += rem;
            N = N / 10;
        }
        while (sum > 0) {
            rem = sum % 2;
            binary = rem + binary;
            sum = sum / 2;
        }
        return binary;
    }

    public static void main(String[] args) {
        System.out.println(solve(1000));
        System.out.println(solve(150));
        System.out.println(solve(147));
    }
}

/*
Output:
1
110
1100
*/

//src/main/resources/c/digits_sum_in_binary/Solution.py
def solve(N):
    sum = 0
    binary = ""
    while N > 0:
        sum += N % 10
        N = N // 10
    while sum > 0:
        binary = str(sum % 2) + binary
        sum = sum // 2
   