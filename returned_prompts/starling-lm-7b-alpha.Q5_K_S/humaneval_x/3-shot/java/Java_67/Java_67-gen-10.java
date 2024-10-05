        String[] split = s.split(" ");
        int apples = Integer.parseInt(split[0].substring(0, split[0].length() - 1));
        int oranges = Integer.parseInt(split[1].substring(0, split[1].length() - 1));
        return n - apples - oranges;
    }
}

