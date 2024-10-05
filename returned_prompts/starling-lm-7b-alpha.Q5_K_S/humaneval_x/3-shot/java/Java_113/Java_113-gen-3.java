        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                int d = Integer.parseInt(c + "");
                if ((d & 1) == 1) count += 1;
            }
            result.add(String.format("the number of odd elements %dn the str%ring %d of the %d%n", count, s.length(), s.length(), lst.size()));
        }
        return result;
    }
}

