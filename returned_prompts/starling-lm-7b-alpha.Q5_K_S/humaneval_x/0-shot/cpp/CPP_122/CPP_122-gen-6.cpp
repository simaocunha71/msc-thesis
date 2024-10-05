    int sum = 0;
    for(int i = 0; i < k; i++) {
        if(arr[i] <= 99)
            sum += arr[i];
    }
    return sum;
}
int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    int sum = add_elements(arr,k);
    printf("%d",sum);
    return 0;
}







*/
import java.util.*;

public class Solution {
    public static int add_elements(vector<int> arr,int k) {
        int sum = 0;
        for(int i = 0; i < k; i++) {
            if(arr[i] <= 99)
                sum += arr[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        vector<int> arr = new vector<int>();
        arr.add(111);
        arr.add(21);
        arr.add(3);
        arr.add(4000);
        arr.add(5);
        arr.add(6);
        arr.add(7);
        arr.add(8);
        arr.add(9);
        int k = 4;
        int sum = add_elements(arr,k);
        System.out.println(sum);
    }
}
















































































































































