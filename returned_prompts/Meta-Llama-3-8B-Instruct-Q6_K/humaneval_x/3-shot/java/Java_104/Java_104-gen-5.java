        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean isUnique = true;
            for (char c : String.valueOf(num).toCharArray()) {
                if (Integer.parseInt(String.valueOf(c)) % 2 == 0) {
                    isUnique = false;
                    break;
                }
            }
            if (isUnique) result.add(num);
        }
        Collections.sort(result);
        return result;
    }
}