import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> list = new ArrayList<Integer>();
        list.add(1);
        list.add(3);
        list.add(2);
        for(int i=3;i<n+1;i++){
            if(i%2==0){
                list.add(1+(i/2));
            }
            else{
                list.add(list.get(i-2)+list.get(i-1)+list.get(i-1));
            }
        }
        System.out.println(list);
    }
}
