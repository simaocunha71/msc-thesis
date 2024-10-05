        String[] num_str_list = s.split(" ");
        int apples = Integer.parseInt(num_str_list[0]);
        int oranges = Integer.parseInt(num_str_list[1]);
        return n - apples - oranges;
    }
}

