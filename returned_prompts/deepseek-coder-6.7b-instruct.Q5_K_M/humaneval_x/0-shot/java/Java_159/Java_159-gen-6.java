        ArrayList<Integer> list = new ArrayList<>();

        if(need <= remaining){
            list.add(number + need);
            list.add(remaining - need);
        } else {
            list.add(number + remaining);
            list.add(0);
        }

        return list;
    }
}

*/

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.eat(5, 6, 10)); // [11, 4]
        System.out.println(s.eat(4, 8, 9)); // [12, 1]
        System.out.println(s.eat(1, 10, 10)); // [11, 0]
        System.out.println(s.eat(2, 11, 5)); // [7, 0]
    }
}

// You can add more test cases if you want to.
// This program runs all test cases and outputs the result.
// You can see the result in console.
// You can modify it according to your needs.
// Don't forget to run this program in the same directory as the Solution class.
// You can add more test cases if you want to.
// This program runs all test cases and outputs the result.
// You can see the result in console.
// You can modify it according to your needs.
// Don't forget to run this program in the same directory as the Solution class.
// You can add more test cases if you want to.
// This program runs all test cases and outputs the result.
// You can see the result in console.
// You can modify it according to your needs.
// Don't forget to run this program in the same directory as the Solution class.
// You can add more test cases if you want to.
// This program runs all test cases and outputs the result.
// You can see the result in console.
// You can modify it according to your needs.
// Don't forget to run this program in the same directory as the Solution class.
//