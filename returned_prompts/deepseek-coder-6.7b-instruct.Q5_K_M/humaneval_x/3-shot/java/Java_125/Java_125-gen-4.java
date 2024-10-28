        if (txt.contains(" "))  return Arrays.asList(txt.split(" "));
        if (txt.contains(","))  return Arrays.asList(txt.split(","));

        int count = 0;
        for (char c : txt.toCharArray()) {
            if (Character.isLowerCase(c) && (c - 'a') % 2 == 1) count++;
        }
        return count;
     }
}

