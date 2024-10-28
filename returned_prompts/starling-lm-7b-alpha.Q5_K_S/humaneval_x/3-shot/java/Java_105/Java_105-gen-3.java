        Collections.sort(arr);
        Collections.reverse(arr);
        List<String> result = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            result.add(byLength.get(arr.get(i)));
        }
        return result;
    }

    public static String[] byLength = {
        "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    };
}

