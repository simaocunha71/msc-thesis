        List<List<Integer>> result = new ArrayList<>();

        // Sort row by rows in ascending order
        lst.sort(Comparator.comparingInt(list -> list.get(0)));

        // Sort coordinates of the row by columns in descending order
        for (List<Integer> row : lst) {
            row.sort(Comparator.comparingInt(col -> col).reversed());
        }

        // Search for integer x in the list
        for (List<Integer> row : lst) {
            for (int i = 0; i < row.size(); i++) {
                if (row.get(i) == x) {
                    result.add(new ArrayList<Integer>() {{
                        add(i);
                        add(lst.indexOf(row));
                    }});
                }
            }
        }
        return result;
    }
}

