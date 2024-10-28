        List<Integer> result = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            String s = i + "";
            for (char c : s.toCharArray()) {
                if (c % 2 == 0) result.add(c - '0');
            }
        }
        Collections.sort(result);
        return result;
    }
}

