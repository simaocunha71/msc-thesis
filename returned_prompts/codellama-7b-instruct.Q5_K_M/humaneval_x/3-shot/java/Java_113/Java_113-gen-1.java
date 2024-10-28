        List<Integer> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if (c % 2 == 1) count++;
            }
            result.add(count);
        }
        return result;
    }
}

