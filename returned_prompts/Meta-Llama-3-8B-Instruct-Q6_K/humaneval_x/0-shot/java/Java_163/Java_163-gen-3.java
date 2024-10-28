        List<Integer> result = new ArrayList<>();
        for (int i = Math.min(a, b); i <= Math.max(a, b); i++) {
            String s = Integer.toString(i);
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) % 2 == 0) {
                    result.add(Integer.parseInt(s.substring(j, j + 1)));
                }
            }
        }
        return result;
    }

