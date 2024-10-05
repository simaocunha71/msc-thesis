        List<String> result = new ArrayList<>();
        List<Integer> sorted = new ArrayList<>(arr);
        Collections.sort(sorted);
        Collections.reverse(sorted);

        for (int i : sorted) {
            if (i >= 1 && i <= 9) {
                result.add(String.valueOf(i));
            }
        }
        return result;
    }
}

