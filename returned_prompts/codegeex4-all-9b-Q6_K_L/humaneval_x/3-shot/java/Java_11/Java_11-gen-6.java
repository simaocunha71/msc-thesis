        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < Math.min(a.length(), b.length()); i++) {
            if (a.charAt(i) == b.charAt(i)) {
                sb.append('0');
            } else {
                sb.append('1');
            }
        }

        return sb.toString();
    }
}

