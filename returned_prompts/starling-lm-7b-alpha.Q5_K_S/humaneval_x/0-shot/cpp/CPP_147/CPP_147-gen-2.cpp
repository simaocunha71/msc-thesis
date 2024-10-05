    int count = 0;
    for(int i = 1; i <= n; i++)
    {
        for(int j = i + 1; j <= n; j++)
        {
            for(int k = j + 1; k <= n; k++)
            {
                int a = i * i - i + 1;
                int b = j * j - j + 1;
                int c = k * k - k + 1;
                if((a + b + c) % 3 == 0)
                {
                    count++;
                }
            }
        }
    }
    return count;
}
int main()
{
    int n;
    scanf("%d", &n);
    printf("%d\n", get_matrix_triples(n));
    return 0;
}

*/
import java.util.*;
public class Solution {
    public int get_matrix_triples(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                for (int k = j + 1; k <= n; k++) {
                    int a = i * i - i + 1;
                    int b = j * j - j + 1;
                    int c = k * k - k + 1;
                    if ((a + b + c) % 3 == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(s.get_matrix_triples(n));
    }
}


















































