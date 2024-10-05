        Collections.sort(arr, (i, j) -> Integer.compare(countOnes(i), countOnes(j)) != 0 ?
                Integer.compare(countOnes(i), countOnes(j)) : Integer.compare(i, j));
        return arr;
    }

    private int countOnes(int i) {
        int result = 0;
        while (i > 0) {
            if (i % 2 == 1) result += 1;
            i /= 2;
        }
        return result;
    }
}


public class Kata {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.sortArray(Arrays.asList(1, 5, 2, 3, 4)));
    }
}
```