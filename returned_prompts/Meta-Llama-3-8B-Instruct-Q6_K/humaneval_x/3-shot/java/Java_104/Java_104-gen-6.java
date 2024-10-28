        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean is_valid = true;
            for (char c : String.valueOf(num).toCharArray()) {
                if (Integer.parseInt(String.valueOf(c)) % 2 == 0) {
                    is_valid = false;
                    break;
                }
            }
            if (is_valid) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}

