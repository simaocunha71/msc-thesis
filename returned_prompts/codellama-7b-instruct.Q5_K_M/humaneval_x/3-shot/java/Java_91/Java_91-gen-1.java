        int result = 0;
        for (String sentence : S.split("[.?!]")) {
            if (sentence.startsWith("I")) result++;
        }
        return result;
    }
}

