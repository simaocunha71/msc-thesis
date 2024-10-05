        List<Integer> sorted_and_reversed = new ArrayList<>(arr);
        Collections.sort(sorted_and_reversed);
        Collections.reverse(sorted_and_reversed);

        List<Integer> result = new ArrayList<>();
        for (Integer i : sorted_and_reversed) {
            if (i >= 1 && i <= 9) result.add(i);
        }

        List<String> result_str = new ArrayList<>();
        for (Integer i : result) {
            result_str.add(one_to_nine.get(i));
        }
        return result_str;
    }
}

class one_to_nine {
    static Map<Integer, String> one_to_nine = new HashMap<>();
    static {
        one_to_nine.put(1, "One");
        one_to_nine.put(2, "Two");
        one_to_nine.put(3, "Three");
        one_to_nine.put(4, "Four");
        one_to_nine.put(5, "Five");
        one_to_nine.put(6, "Six");
        one_to_nine.put(7, "Seven");
        one_to_nine.put(8, "Eight");
        one_to_nine.put(9, "Nine");
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        //test();
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));

        List<Integer> arr = Arrays.asList(1, -1, 55);
        List<String> result = solution.byLength(arr);
        System.out.println(result);
   