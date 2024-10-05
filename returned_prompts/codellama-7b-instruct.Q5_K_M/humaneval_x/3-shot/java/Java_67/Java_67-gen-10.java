        String[] arr = s.split(" and ");
        String[] apples = arr[0].split(" ");
        String[] oranges = arr[1].split(" ");
        int apples_num = Integer.parseInt(apples[0]);
        int oranges_num = Integer.parseInt(oranges[0]);
        return n - apples_num - oranges_num;
    }
}

