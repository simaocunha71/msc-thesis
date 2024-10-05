import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int ans=0;
        int i=1;
        while(i<=n)
        {
            if(i==k)
            {
                ans++;
            }
            i++;
        }
        System.out.println(ans);
    }
}

