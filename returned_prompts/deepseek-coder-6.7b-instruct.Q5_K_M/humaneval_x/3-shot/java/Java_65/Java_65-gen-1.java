        StringBuilder sb = new StringBuilder(String.valueOf(x));
        int len = sb.length();
        if (shift > len) {
            return sb.reverse().toString();
        }
        StringBuilder result = new StringBuilder(sb.substring(len - shift));
        result.append(sb.substring(0, len - shift));
        return result.toString();

     }
}

