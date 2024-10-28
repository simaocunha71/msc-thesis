    vector<int> primes;
    for(int i = 2; i<n; i++){
        bool isPrime = true;
        for(int j = 2; j<i; j++){
            if(i%j==0){
                isPrime = false;
                break;
            }
        }
        if(isPrime){
            primes.push_back(i);
        }
    }
    return primes;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> primes = count_up_to(n);
    int l = primes.size();
    for(int i = 0; i<l; i++){
        printf("%d ", primes[i]);
    }
    printf("\n");
    return 0;
}

*/
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> primes = count_up_to(n);
        int l = primes.size();
        for(int i = 0; i<l; i++){
            System.out.print(primes.get(i) + " ");
        }
        System.out.println();
    }

    public static ArrayList<Integer> count_up_to(int n) {
        ArrayList<Integer> primes = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            boolean isPrime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(i);
            }
        }
        return primes;
    }
}





































