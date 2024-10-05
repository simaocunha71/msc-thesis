        int count = 0;
        for (String s : S.split("[.?!]")) {
            if (s.startsWith("I")) count += 1;
        }
        return count;
    }
}

