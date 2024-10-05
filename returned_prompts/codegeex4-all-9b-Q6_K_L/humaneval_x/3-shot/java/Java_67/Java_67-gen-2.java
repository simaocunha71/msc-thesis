        int apples = Integer.parseInt(s.substring(0, s.indexOf(" ")));
        int oranges = Integer.parseInt(s.substring(s.indexOf(" ") + 5, s.indexOf("o")));
        return n - apples - oranges;
    }
}

