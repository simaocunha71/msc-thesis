import java.util.*;
import java.lang.*;

class Solution {
    public int isBored(String S) {

        // Split the string into sentences
        String[] sentences = S.split("[.?!]");

        // Initialize the boredom count
        int boredom = 0;

        // Loop through each sentence
        for (String sentence : sentences) {
            // Check if the sentence starts with "I"
            if (sentence.trim().startsWith("I")) {
                // Increment the boredom count
                boredom++;
            }
        }

        // Return the boredom count
        return boredom;
    }
}