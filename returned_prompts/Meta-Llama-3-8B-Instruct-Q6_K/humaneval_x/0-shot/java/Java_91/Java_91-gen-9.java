    int boredomCount = 0;
    String[] sentences = S.split("[.!?]");
    for (String sentence : sentences) {
        sentence = sentence.trim();
        if (sentence.length() > 0 && sentence.substring(0, 2).equals("I ")) {
            boredomCount++;
        }
    }
    return boredomCount;
}  // This is the solution for the problem. It counts the number of boredoms in a given string of words.

