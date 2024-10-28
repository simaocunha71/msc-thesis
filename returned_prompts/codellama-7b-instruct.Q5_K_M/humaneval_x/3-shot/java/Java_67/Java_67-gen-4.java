        String[] s_list = s.split(" and ");
        int apples = Integer.parseInt(s_list[0]);
        int oranges = Integer.parseInt(s_list[1]);
        return n - apples - oranges;
    }
}

