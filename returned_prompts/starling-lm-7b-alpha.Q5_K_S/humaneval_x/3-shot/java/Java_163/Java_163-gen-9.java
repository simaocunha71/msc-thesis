        List<Integer> result = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            String num = Integer.toString(i);
            for (int j = 0; j < num.length(); j++) {
                if (num.charAt(j) % 2 == 0) {
                    result.add(i);
                }
            }
        }
        return result;
    }
}

