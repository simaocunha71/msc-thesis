        List<Integer> result = new ArrayList<>();
        for (int i = Math.min(a, b); i <= Math.max(a, b); i++) {
            String i_string = Integer.toString(i);
            for (int j = 0; j < i_string.length(); j++) {
                int digit = Integer.parseInt(String.valueOf(i_string.charAt(j)));
                if (digit % 2 == 0) result.add(digit);
            }
        }
        return result;
    }
}

