    StringBuilder sb = new StringBuilder();

    String[] words = s.split(" ");
    for (String word : words) {
        char[] chars = word.toCharArray();
        Arrays.sort(chars);
        sb.append(chars);
        sb.append(" ");
    }
    return sb.toString();
    }
}














```