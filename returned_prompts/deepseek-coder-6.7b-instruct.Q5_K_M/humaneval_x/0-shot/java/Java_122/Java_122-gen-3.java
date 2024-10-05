        int sum = 0;
        for(int i = 0; i < k; i++){
            if(arr.get(i) >= 0 && arr.get(i) <= 99){
                sum += arr.get(i);
            }
        }
        return sum;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> arr = Arrays.asList(111, 21, 3, 4000, 5, 6, 7, 8, 9);
        int k = 4;
        System.out.println(solution.addElements(arr, k)); // Output: 24
    }
}