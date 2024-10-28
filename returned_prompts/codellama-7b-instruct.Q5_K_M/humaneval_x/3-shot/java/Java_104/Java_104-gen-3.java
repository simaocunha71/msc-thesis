        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            String s = String.valueOf(i);
            for (char c : s.toCharArray()) {
                if (c % 2 == 0) continue A;
            }
            result.add(i);
        }
        Collections.sort(result);
        return result;
    }
}

