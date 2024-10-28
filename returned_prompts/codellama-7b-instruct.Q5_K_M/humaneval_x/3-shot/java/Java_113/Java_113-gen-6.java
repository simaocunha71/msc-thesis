        List<Integer> result = new ArrayList<>();
        for (String str : lst) {
            int count = 0;
            for (char c : str.toCharArray()) {
                if (c % 2 == 1) count += 1;
            }
            result.add(count);
        }
        return result;
    }
}

