        List<Integer> sorted_arr = new ArrayList<>(arr);
        sorted_arr.sort(Integer::compareTo);
        sorted_arr.reverse();
        List<String> result = new ArrayList<>();
        for (int i = 0; i < sorted_arr.size(); i++) {
            if (sorted_arr.get(i) >= 1 && sorted_arr.get(i) <= 9)
                result.add(sorted_arr.get(i).toString());
        }
        return result;

    }
}

