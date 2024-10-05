        List<Integer> result = new ArrayList<>(arr);

        for (int i = 0; i < k; i++) {
            int max = Integer.MIN_VALUE;
            for (int j = 0; j < result.size(); j++) {
                if (result.get(j) > max) max = result.get(j);
            }
            result.remove(Integer.valueOf(max));
        }

        return result;
    }
}

