        StringBuilder result = new StringBuilder();
        for(int i = 0; i <= n; i++) {
            result.append(i);
            if(i != n) {
                result.append(" ");
            }
        }
        return result.toString();
    }
}

