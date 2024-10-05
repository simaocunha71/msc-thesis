        int result = 0;
        String[] sentences = S.split("[.?!]");

        for (String sentence : sentences) {
            if (sentence.startsWith("I")) result += 1;
        }
        return result;
    }
}

