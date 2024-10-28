    if(N==0)
        return "";
    if(N%2==1)
        return "1"+solve(N/2);
    else
        return "0"+solve(N/2);
}
int main(){
    int N;
    scanf("%d",&N);
    printf("%s\n",solve(N).c_str());
}















*/
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        System.out.println(solve(n));
    }

    public static String solve(int n) {
        if (n == 0) return "";
        if (n % 2 == 1) return "1" + solve(n / 2);
        else return "0" + solve(n / 2);
    }
}

```
