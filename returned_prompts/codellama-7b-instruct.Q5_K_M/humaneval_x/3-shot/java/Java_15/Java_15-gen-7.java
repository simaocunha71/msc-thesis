        StringBuilder result = new StringBuilder();
        for (int i = 0; i <= n; i++) {
            if (result.length() > 0) result.append(" ");
            result.append(i);
        }
        return result.toString();
    }
}

