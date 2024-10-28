        String[] parts = s.split(" and ");
        int oranges = Integer.parseInt(parts[1].split(" ")[0]);
        return n - Integer.parseInt(parts[0].split(" ")[0]) - oranges;
    }
}

