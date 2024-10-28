        Map<String, Integer> m = new HashMap<>();

        for (int i = 0; i < test.length(); i++) {
            if (m.containsKey(String.valueOf(test.charAt(i)))) {
                m.put(String.valueOf(test.charAt(i)), m.get(String.valueOf(test.charAt(i))) + 1);
            } else {
                m.put(String.valueOf(test.charAt(i)), 1);
            }
        }

        List<String> keys = new ArrayList<>(m.keySet());
        List<Integer> values = new ArrayList<>(m.values());

        Collections.sort(keys);
        Collections.sort(values);

        Map<String, Integer> res = new HashMap<>();

        for (int i = keys.size() - 1; i >= 0; i--) {
            if (values.get(i) == values.get(values.size() - 1)) {
                res.put(keys.get(i), values.get(i));
            }
        }

        return res;
    }
}


































```