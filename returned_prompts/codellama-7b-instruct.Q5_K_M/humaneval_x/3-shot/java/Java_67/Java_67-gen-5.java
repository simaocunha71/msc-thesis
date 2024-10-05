        String[] s_array = s.split("\\s+");
        int apples = Integer.parseInt(s_array[0]);
        int oranges = Integer.parseInt(s_array[2]);

        return n - apples - oranges;
    }
}

