    for(int i=0;i<l.size()-1;i++)
        if(l[i+1]<l[i])
            return false;
    return true;
}

int main(){
    vector<float> l={1, 2, 4, 20};
    printf("%d\n",monotonic(l));
    l={1, 20, 4, 10};
    printf("%d\n",monotonic(l));
    l={4, 1, 0, -10};
    printf("%d\n",monotonic(l));
    return 0;
}

*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }
        System.out.println(monotonic(arr));
    }

    public static boolean monotonic(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i + 1] < arr[i]) {
                return false;
            }
        }
        return true;
    }
}









































































































































































