    vector<int>prime;
    for(int i = 2; i < n; i++)
    {
        bool is_prime = true;
        for(int j = 2; j < i; j++)
        {
            if(i % j == 0)
            {
                is_prime = false;
                break;
            }
        }
        if(is_prime)
        {
            prime.push_back(i);
        }
    }
    return prime;
}
int main(){
    int n;
    cin >> n;
    vector<int>prime = count_up_to(n);
    for(int i = 0; i < prime.size(); i++)
    {
        cout << prime[i] << " ";
    }
    cout << endl;
    return 0;
}




*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        ArrayList<Integer>prime = count_up_to(n);
        for(int i = 0; i < prime.size(); i++) {
            System.out.print(prime.get(i) + " ");
        }
        System.out.println();
    }
    public static ArrayList<Integer> count_up_to(int n) {
        ArrayList<Integer>prime = new ArrayList<>();
        for(int i = 2; i < n; i++) {
            boolean is_prime = true;
            for(int j = 2; j < i; j++) {
                if(i % j == 0) {
                    is_prime = false;
                    break;
                }
            }
            if(is_prime) {
                prime.add(i);
            }
        }
        return prime;
    }
}


















































