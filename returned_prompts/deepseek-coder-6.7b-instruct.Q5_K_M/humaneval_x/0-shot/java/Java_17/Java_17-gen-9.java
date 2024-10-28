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

This solution works by splitting the input string into an array of notes. It then iterates over each note and adds the corresponding number of beats to the list. The result is a list of integers representing how many beats each note lasts.
    */

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.parseMusic("o o| .| o| o| .| .| .| .| o o")); // Outputs: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    }
}








































































































































































































































