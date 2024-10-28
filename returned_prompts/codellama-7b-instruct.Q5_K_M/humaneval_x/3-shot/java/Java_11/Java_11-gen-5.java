        StringBuilder result = new StringBuilder();

        for (int i = 0; i < Math.min(a.length(), b.length()); i++) {
            result.append((a.charAt(i) == b.charAt(i) ? "0" : "1"));
        }

        return result.toString();
    }
}

