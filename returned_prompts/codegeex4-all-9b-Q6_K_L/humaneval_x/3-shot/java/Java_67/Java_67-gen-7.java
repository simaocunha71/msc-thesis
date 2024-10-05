        int apples = Integer.parseInt(s.replaceAll("[^0-9]", "").split(" ")[0]);
        int oranges = Integer.parseInt(s.replaceAll("[^0-9]", "").split(" ")[2]);
        return n - apples - oranges;
    }
}

