        if (a < 0)
            a = -a;

        int i = 0;
        while (i * i * i <= a) {
            if (i * i * i == a)
                return true;
            i++;
        }
        return false;
    }
}

Explanation:
In this code, we first check if the absolute value of the input number 'a' is a perfect cube or not. If 'a' is negative, we convert it to its absolute value. Then we initialize an integer 'i' to 0, and use a while loop to iterate through all the numbers starting from 0 until we find a number whose cube is less than or equal to 'a'. If we find such a number, we check if its cube is equal to 'a'. If it is, we return true, indicating that 'a' is a cube of some integer. If we reach the end of the loop without finding such a number, we return false, indicating that 'a' is not a cube of any integer.
 */
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.iscube(1)); // true
        System.out.println(s.iscube(2)); // false
        System.out.println(s.iscube(-1)); // true
        System.out.println(s.iscube(64)); // true
        System.out.println(s.iscube(0)); // true
        System.out.println(s.iscube(180)); // false
    }
}

This code should work for all the test cases you mentioned.
 */
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.iscube(1)); // true
        System.out.println(s.iscube(2)); // false
        System.out.println(s.iscube(-1)); // true
        System.out.println(s.iscube(64)); // true
        System.out.println(s.iscube(0)); // true
        System.out.println(s