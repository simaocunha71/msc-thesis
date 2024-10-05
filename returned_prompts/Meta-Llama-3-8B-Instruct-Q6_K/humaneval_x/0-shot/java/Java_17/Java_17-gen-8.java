    import java.util.*;

    class Solution {
        public List<Integer> parseMusic(String string) {
            List<Integer> result = new ArrayList<>();
            String[] notes = string.split(" ");
            for (String note : notes) {
                if (note.equals("o")) {
                    result.add(4);
                } else if (note.equals("o|")) {
                    result.add(2);
                } else if (note.equals(".|")) {
                    result.add(1);
                }
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "o o| .| o| o| .| .| .| .| o o";
        List<Integer> result = solution.parseMusic(s);
        for (Integer beat : result) {
            System.out.println(beat);
        }
    }
    >>> 4
    >>> 4
    >>> 1
    >>> 2
    >>> 2
    >>> 1
    >>> 1
    >>> 1
    >>> 1
    >>> 4
    >>> 4
    Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

