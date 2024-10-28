        List<Integer> result = new ArrayList<>();
        StringBuilder note_string = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (c == 'o' || c == 'o|' || c == '.|') {
                note_string.append(c);
            } else {
                result.add(parseIntNote(note_string));
                note_string.setLength(0);
            }
        }
        result.add(parseIntNote(note_string));
        return result;
    }

    private int parseIntNote(StringBuilder note_string) {
        int result = 0;
        if (note_string.length() == 1) {
            result = 4;
        } else if (note_string.length() == 2) {
            result = 2;
        } else {
            result = 1;
        }
        return result;
    }
}


class Input {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // hasCloseElements
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));

        // separateParenGroups
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));

        // truncateNumber
        System.out.println(solution.truncateNumber(3.5));

        // parseMusic
        System.out.println(solution.parseMusic("o o| .| o| o| o"));
        System.out.println(solution.parseMusic("o o| .| o| o| .| .| .| .| o o"));
    }
}
```