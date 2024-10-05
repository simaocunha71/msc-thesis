	if(n==0 || n==1 || n==2)
		return n;
	else
	{
		int a = 0;
		int b = 0;
		int c = 1;
		int i = 3;
		while(i<n)
		{
			a = b;
			b = c;
			c = a + b;
			i++;
		}
		return c;
	}
}
int main()
{
	printf("%d\n",fibfib(8));
	return 0;
}









*/
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.println(fibfib(n));
    }
    public static int fibfib(int n) {
        if (n == 0 || n == 1 || n == 2) {
            return n;
        } else {
            int a = 0;
            int b = 0;
            int c = 1;
            int i = 3;
            while (i < n) {
                a = b;
                b = c;
                c = a + b;
                i++;
            }
            return c;
        }
    }
}









*/

```
