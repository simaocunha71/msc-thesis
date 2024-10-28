        String result = Integer.toString(x);
        List<Character> result_list = new ArrayList<>();
        for (char c : result.toCharArray()) {
            result_list.add(c);
        }

        if (shift >= result_list.size()) {
            Collections.reverse(result_list);
            return new String(result_list.toArray(new Character[0]));
        }

        for (int i = 0; i < shift; i++) {
            result_list.add(result_list.remove(0));
        }

        return new String(result_list.toArray(new Character[0]));

    }
}

