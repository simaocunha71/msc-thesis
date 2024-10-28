        int oddCountLst1 = 0;
        int oddCountLst2 = 0;

        for(int i = 0; i < lst1.size(); i++){
            if(lst1.get(i) % 2 != 0){
                oddCountLst1++;
            }
        }

        for(int i = 0; i < lst2.size(); i++){
            if(lst2.get(i) % 2 != 0){
                oddCountLst2++;
            }
        }

        if(oddCountLst1 > oddCountLst2){
            return "NO";
        } else {
            return "YES";
        }
    }
}

*/

//Explanation:
//Firstly, we calculate the count of odd numbers in lst1 and lst2.
//If the count of odd numbers in lst1 is more than the count of odd numbers in lst2,
//then it is impossible to make all the numbers in lst1 even by exchanging elements from lst1 and lst2.
//Therefore, we return "NO".
//Otherwise, it is possible to make all the numbers in lst1 even by exchanging elements from lst1 and lst2.
//Therefore, we return "YES".
//This solution assumes that the numbers in lst2 are positive.
//If lst2 can have negative numbers, we can add a condition to check if the negative numbers in lst2 are odd.
//If so, we increase the count of odd numbers in lst2.
//This way, we can make sure that we can exchange the odd numbers in lst2 to even numbers in lst1.
//This solution has a time complexity of O(n), where n is the size of the input lists.

//Code:
/*
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 2, 3, 4))); // "YES"
        System.out