        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < x.size(); i++) {
            if (x.get(i) % 2 == 1) {
                boolean is_valid = true;
                for (int j = 0; j < x.get(i).toString().length(); j++) {
                    if (x.get(i) % (int) Math.pow(10, j + 1) / (int) Math.pow(10, j) % 2 == 0) {
                        is_valid = false;
                        break;
                    }
                }
                if (is_valid) result.add(x.get(i));
            }
        }
        Collections.sort(result);
        return result;
    }
}

