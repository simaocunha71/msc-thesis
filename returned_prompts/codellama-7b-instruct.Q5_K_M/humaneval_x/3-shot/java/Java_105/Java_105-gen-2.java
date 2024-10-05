        List<String> result = new ArrayList<>();
        List<Integer> sorted_arr = new ArrayList<>(arr);
        sorted_arr.sort(Integer::compareTo);
        sorted_arr.reverse();

        for (int i : sorted_arr) {
            if (i >= 1 && i <= 9) result.add(i + "");
        }

        return result;
    }
}

