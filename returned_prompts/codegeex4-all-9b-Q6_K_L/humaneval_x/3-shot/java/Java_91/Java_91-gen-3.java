        String[] sentences = S.split("[.?!]");
        int result = 0;
        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) result += 1;
        }
        return result;
    }
}

