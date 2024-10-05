        List<Integer> result = byLength(arr);
        List<String> names = Arrays.asList("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine");
        List<String> result_names = new ArrayList<>();
        for (int i = 0; i < result.size(); i++) {
            result_names.add(names.get(result.get(i) - 1));
        }
        return result_names;
    }
}

