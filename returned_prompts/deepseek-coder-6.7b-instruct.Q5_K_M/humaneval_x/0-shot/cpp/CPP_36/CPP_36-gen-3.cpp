    int count = 0;
    for(int i=1; i<n; i++){
        if(i%11 == 0 || i%13 == 0){
            char buffer[50];
            sprintf(buffer, "%d", i);
            for(int j=0; buffer[j] != '\0'; j++){
                if(buffer[j] == '7'){
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}
int main(){
    printf("%d\n", fizz_buzz(50));  //0
    printf("%d\n", fizz_buzz(78));  //2
    printf("%d\n", fizz_buzz(79));  //3
    return 0;
}

*/

```

## C++

```cpp
#include<iostream>
#include<string>
using namespace std;
int fizz_buzz(int n){
    int count = 0;
    for(int i=1; i<n; i++){
        if(i%11 == 0 || i%13 == 0){
            string number = to_string(i);
            for(int j=0; j<number.length(); j++){
                if(number[j] == '7'){
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}
int main(){
    cout<<fizz_buzz(50)<<endl;  //0
    cout<<fizz_buzz(78)<<endl;  //2
    cout<<fizz_buzz(79)<<endl;  //3
    return 0;
}
```

## Java

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(fizz_buzz(50));  //0
        System.out.println(fizz_buzz(78));  //2
        System.out.println(fizz_buzz(79));  //3
   