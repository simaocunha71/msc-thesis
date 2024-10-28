        List<Integer> result = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            for (int j = 0; j < Integer.toString(i).length(); j++) {
                if (Integer.toString(i).charAt(j) % 2 == 0) {
                    result.add(i);
                }
            }
        }
        return result;
    }
}

