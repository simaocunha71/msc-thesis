        Map<String, Integer> result = new HashMap<>();
        String[] arr = test.split(" ");
        int max = 0;

        for (String s : arr) {
            int count = 0;
            for (String str : arr) {
                if (str.equals(s)) count += 1;
            }

            if (count > max) {
                max = count;
                result.clear();
                result.put(s, count);
            } else if (count == max) {
                result.put(s, count);
            }
        }
        return result;

    }
}

