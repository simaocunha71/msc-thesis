        StringBuilder result = new StringBuilder();
        for (int i = 0; i <= n; i++) {
            result.append(i).append(" ");
        }
        if (result.length() > 0) {
            result.deleteCharAt(result.length() - 1);
        }
        return result.toString();
    }
}

