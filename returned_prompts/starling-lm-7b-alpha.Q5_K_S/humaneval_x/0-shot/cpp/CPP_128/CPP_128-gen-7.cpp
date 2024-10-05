    int product = 1;
    int sum = 0;
    for (int i = 0; i < arr.size(); i++) {
        if(arr[i] == 0) {
            product *= 0;
            continue;
        }
        if(arr[i] < 0) {
            product *= -1;
        } else if(arr[i] > 0) {
            product *= 1;
        }
        sum += abs(arr[i]);
    }
    if(product == 0) {
        return -32768;
    }
    return product * sum;
}



/*
You are given a vector arr of integers and you need to return
sum of magnitudes of integers multiplied by product of all signs
of each number in the vector, represented by 1, -1 or 0.
Note: return -32768 for empty arr.

Example:
>>> prod_signs({1, 2, 2, -4}) == -9
>>> prod_signs({0, 1}) == 0
>>> prod_signs({}) == -32768
*/



int main(){
    vector<int> arr = {1, 2, 2, -4};
    printf("%d\n", prod_signs(arr));
}




























*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = {1, 2, 2, -4};
        System.out.println(prod_signs(arr));
    }
    public static int prod_signs(int[] arr) {
        int product = 1;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == 0) {
                product *= 0;
                continue;
            }
            if(arr[i] < 