        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            String temp = String.valueOf(i);
            boolean is_even = false;
            for (char c : temp.toCharArray()) {
                if ((int) c % 2 == 0) {
                    is_even = true;
                    break;
                }
            }
            if (!is_even) result.add(i);
        }
        Collections.sort(result);
        return result;
    }
}

