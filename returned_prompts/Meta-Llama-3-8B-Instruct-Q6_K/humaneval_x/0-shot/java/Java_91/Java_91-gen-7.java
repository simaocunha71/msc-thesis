    int boredomCount = 0;

    // Split the input string into sentences
    String[] sentences = S.split("[.!?]+");

    // Iterate over each sentence
    for (String sentence : sentences) {
        // Check if the sentence starts with "I"
        if (sentence.trim().startsWith("I")) {
            // If it does, increment the boredom count
            boredomCount++;
        }
    }

    // Return the boredom count
    return boredomCount;
}
