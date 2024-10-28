        int sum = 0;
        for(int i = 1; i < lst.size(); i += 2){
            if(lst.get(i) % 2 == 0){
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.add(Arrays.asList(4, 2, 6, 7))); // 2
        System.out.println(solution.add(Arrays.asList(1, 2, 3, 4, 5, 6))); // 4
        System.out.println(solution.add(Arrays.asList(7, 2, 12, 9, 1, 5))); // 20
    }
}

/*
Output:
2
4
20
*/