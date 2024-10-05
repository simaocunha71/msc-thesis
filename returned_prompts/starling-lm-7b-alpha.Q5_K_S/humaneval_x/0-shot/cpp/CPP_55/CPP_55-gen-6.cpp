	if(n == 0){
		goto B;
	}
	if(n == 1){
		goto C;
	}
	int a = 1, b = 1, c;
	while(n--){
		c = a + b;
		a = b;
		b = c;
	}
	goto D;
B:
	printf("0\n");
	goto E;
C:
	printf("1\n");
	goto E;
D:
	printf("%d\n", a);
E:
	return 0;
}

int main(){
	fib(10);
	return 0;
}




*/
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        System.out.println(fib(n));
    }

    public static int fib(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        int a = 1, b = 1, c;
        while (n-- > 0) {
            c = a + b;
            a = b;
            b = c;
        }
        return a;
    }
}








*/
#include <stdio.h>

int fibo(int n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    int a = 1, b = 1, c;
    while (n-- > 0) {
        c = a + b;
        a = b;
        b = c;
    }
    return a;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", fibo(n));
    return 0;
}


