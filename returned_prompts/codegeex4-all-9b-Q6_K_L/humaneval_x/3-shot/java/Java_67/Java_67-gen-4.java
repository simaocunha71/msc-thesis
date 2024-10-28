        int apples = Integer.parseInt(s.substring(0, s.indexOf(" ")));
        int oranges = Integer.parseInt(s.substring(s.indexOf(" ") + 3, s.indexOf(" ", s.indexOf(" ") + 3)));
        return n - apples - oranges;
    }
}

