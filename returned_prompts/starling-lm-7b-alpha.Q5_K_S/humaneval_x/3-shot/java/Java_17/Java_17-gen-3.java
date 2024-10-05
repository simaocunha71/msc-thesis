        List<Integer> result = new ArrayList<>();
        StringBuilder current_note = new StringBuilder();
        int current_length = 0;

        for (char c : string.toCharArray()) {
            if (c == 'o') {
                current_length = 4;
                current_note.append(c);
            } else if (c == '|') {
                result.add(current_length);
                current_length = 0;
                current_note.setLength(0);
            } else if (c == '.') {
                current_length = 1;
                current_note.append(c);
            } else if (c == ' ') {
                result.add(current_length);
                current_length = 0;
                current_note.setLength(0);
            } else {
                current_length = Integer.parseInt(current_note.toString());
                result.add(current_length);
                current_length = 0;
                current_note.setLength(0);
            }
        }
        result.add(current_length);
        return result;
    }
}


class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(s.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(s.truncateNumber(3.5));
        System.out.println(s.parseMusic("o o| .| o| o| o"));
    }
}

```