        int result = 0;
        boolean boring = false;
        for (String s : S.split("[.?!]")) {
            if (s.startsWith("I")) {
                if (boring) {
                    result += 1;
                }
                boring = true;
            } else {
                boring = false;
            }
        }
        return result;
    }
}

