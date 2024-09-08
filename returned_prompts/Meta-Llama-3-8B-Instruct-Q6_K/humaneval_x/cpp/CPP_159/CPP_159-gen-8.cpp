    int total = number + need;
    int left = remaining - need + number;
    if(left < 0){
        total += remaining;
        left = 0;
    }
    return {total,left};
}  



C++ Code
```C++
#include <iostream>
using namespace std;

int main() {
    int number, need, remaining;
    cout<<"Enter the number of carrots eaten: ";
    cin>>number;
    cout<<"Enter the number of carrots needed: ";
    cin>>need;
    cout<<"Enter the remaining carrots: ";
    cin>>remaining;

    vector<int> result = eat(number, need, remaining);
    cout<<"Total carrots eaten: "<<result[0]<<endl;
    cout<<"Carrots left: "<<result[1]<<endl;
    return 0;
}

```



Python Code

```Python
def eat(number, need, remaining):
    total = number + need
    left = remaining - need + number
    if left < 0:
        total += remaining
        left = 0
    return [total, left]

number = int(input("Enter the number of carrots eaten: "))
need = int(input("Enter the number of carrots needed: "))
remaining = int(input("Enter the remaining carrots: "))

result = eat(number, need, remaining)
print("Total carrots eaten: ", result[0])
print("Carrots left: ", result[1])
```



Java Code

```Java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of carrots eaten: ");
        int number = scanner.nextInt();
        System.out.println("Enter the number of carrots needed: ");
        int need = scanner.nextInt();
        System.out.println("Enter the remaining carrots: ");
        int remaining = scanner.nextInt();

        int[] result = eat(number, need, remaining);
        System.out.println("Total carrots eaten: " + result[0]);
        System.out.println("Carrots left: " + result[1]);
    }

    public static int[] eat(int number, int need, int remaining) {
        int total = number + need;
        int left = remaining - need + number;
        if (left < 0) {
            total += remaining;
            left = 0;
        }
        return new int[]{total, left};
    }
}
```



Test Cases:

1. eat(5, 6