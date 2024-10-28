        List<Integer> result = new ArrayList<>();
        for (int i = Math.min(a, b); i <= Math.max(a, b); i++) {
            String s = i + "";
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                if (c % 2 == 0) {
                    result.add(i);
                }
            }
        }
        return result;
    }
}

