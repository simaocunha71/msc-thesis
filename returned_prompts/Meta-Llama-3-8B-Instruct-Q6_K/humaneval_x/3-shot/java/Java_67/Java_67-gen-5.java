        String[] parts = s.split(" and ");
        String apples = parts[0].split(" ")[0];
        String oranges = parts[1].split(" ")[0];
        int total_apples = Integer.parseInt(apples.replace("apples", ""));
        int total_oranges = Integer.parseInt(oranges.replace("oranges", ""));
        return n - total_apples - total_oranges;
    }
}

