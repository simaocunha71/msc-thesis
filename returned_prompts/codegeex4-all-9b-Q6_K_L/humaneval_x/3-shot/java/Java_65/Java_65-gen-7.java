        String s = String.valueOf(x);
        StringBuilder sb = new StringBuilder(s);

        if (shift >= sb.length()) {
            sb.reverse();
            return sb.toString();
        } else {
            for (int i = 0; i < shift; i++) {
                sb.append(sb.charAt(0));
                sb.deleteCharAt(0);
            }
            return sb.toString();
        }
    }
}

