public class Solution {
    public int isBored(String S) {
        String[] sentences = S.split("[.!?]");
        int boredomCount = 0;
        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) {
                boredomCount++;
            }
        }
        return boredomCount;
    }
}

