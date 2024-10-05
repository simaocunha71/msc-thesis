        int counter = 0;
        String[] sentence = S.split("[.?!]");

        for (String s : sentence) {
            if (s.trim().startsWith("I")) counter += 1;
        }
        return counter;
    }
}

