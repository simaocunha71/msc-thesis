    let balance = 0;
    operations.forEach(operation => {
        balance += operation;
        if (balance < 0) {
            return true;
        }
    });
    return false;
};

module.exports = belowZero;






























*/ => Code Here
import java.util.*;
public class Main
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        boolean val=belowZero(arr);
        if(val==true)
        {
            System.out.println("true");
        }
        else
        {
            System.out.println("false");
        }
    }
    public static boolean belowZero(int arr[])
    {
        int balance=0;
        for(int i=0;i<arr.length;i++)
        {
            balance+=arr[i];
            if(balance<0)
            {
                return true;
            }
        }
        return false;
    }
}







