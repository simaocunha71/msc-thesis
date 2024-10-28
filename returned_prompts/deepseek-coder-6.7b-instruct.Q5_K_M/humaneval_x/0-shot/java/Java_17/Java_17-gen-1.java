        List<Integer> beats = new ArrayList<>();
        String[] notes = string.split(" ");

        for (String note : notes) {
            switch (note) {
                case "o":
                    beats.add(4);
                    break;
                case "o|":
                    beats.add(2);
                    break;
                case ".|":
                    beats.add(1);
                    break;
                default:
                    break;
            }
        }
        return beats;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.parseMusic("o o| .| o| o| .| .| .| .| o o")); // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    }
}