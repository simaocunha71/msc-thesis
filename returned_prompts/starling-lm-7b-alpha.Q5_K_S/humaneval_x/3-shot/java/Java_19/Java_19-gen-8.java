        List<String> number_list = Arrays.asList("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine");
        List<String> sorted_list = new ArrayList<>();
        for (String number : number_list) {
            if (numbers.contains(number)) {
                sorted_list.add(number);
            }
        }
        Collections.sort(sorted_list);
        StringBuilder result = new StringBuilder();
        for (String number : sorted_list) {
            result.append(number);
            result.append(' ');
        }
        return result.toString().substring(0, result.length() - 1);
    }
}


public class Exercise {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(s.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(s.truncateNumber(3.5));
        System.out.println(s.sortNumbers("three one five"));
    }
}

```