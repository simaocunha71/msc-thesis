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
            }
        }

        return beats;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.parseMusic("o o| .| o| o| .| .| .| .| o o"));
    }
}

This solution works by first splitting the input string into an array of individual notes. Then it iterates over each note in the array and adds the corresponding number of beats to the list. This is done using a switch statement. Finally, the list of beats is returned.
*/

//