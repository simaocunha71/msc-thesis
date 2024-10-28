        List<String> result = new ArrayList<>();
        for (String str : lst) {
            int count = 0;
            for (char c : str.toCharArray()) {
                if (c % 2 != 0) count += 1;
            }
            result.add(String.format("the number of odd elements %d in the string %d of the input.", count, str));
        }
        return result;
    }
}

