        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= n; i++) {
            sb.append(i);
            if (i != n) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}

