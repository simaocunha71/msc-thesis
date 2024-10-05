        List<String> result = new ArrayList<>();
        for (String str : lst) {
            int count = 0;
            StringBuilder sb = new StringBuilder();
            for (char c : str.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    count++;
                }
                sb.append(c);
            }
            result.add("the number of odd elements " + count + "n the str" + sb + " of the nput.");
        }
        return result;
    }
}

