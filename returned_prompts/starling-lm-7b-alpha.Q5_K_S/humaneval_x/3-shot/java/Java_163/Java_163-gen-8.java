        List<Integer> result = new ArrayList<>();
        for (int i = Math.min(a, b); i <= Math.max(a, b); i++) {
            String integer = Integer.toString(i);
            for (int j = 0; j < integer.length(); j++) {
                if (Integer.parseInt(integer.charAt(j) + "") % 2 == 0) {
                    result.add(Integer.parseInt(integer.charAt(j) + ""));
                }
            }
        }
        Collections.sort(result);
        return result;
    }
}

