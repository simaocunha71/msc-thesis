        String[] parts = s.split(" ");
        int oranges = Integer.parseInt(parts[1]);
        int apples = Integer.parseInt(parts[0]);
        return n - (oranges + apples);
    }
}

