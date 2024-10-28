        for (int i = 0, j = text.length() - 1; i < j; i++, j--) {
            if (text.charAt(i) != text.charAt(j)) return false;
        }
        return true;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String[] input = scanner.nextLine().split(" ");
            switch (input[0]) {
                case "hasCloseElements": {
                    List<Double> numbers = new ArrayList<>();
                    for (String s : input[1].split(",")) {
                        numbers.add(Double.parseDouble(s));
                    }
                    System.out.println(solution.hasCloseElements(numbers, Double.parseDouble(input[2])));
                    break;
                }
                case "separateParenGroups": {
                    System.out.println(Arrays.toString(solution.separateParenGroups(input[1])));
                    break;
                }
                case "truncateNumber": {
                    System.out.println(solution.truncateNumber(Double.parseDouble(input[1])));
                    break;
                }
                case "isPalindrome": {
                    System.out.println(solution.isPalindrome(input[1]));
                    break;
                }
                default: {
                    System.out.println("Unknown command");
                }
            }
        }
    }
}
```