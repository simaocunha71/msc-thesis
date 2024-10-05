        int result = 0;
        for (int i = 0; i < Math.min(k, arr.size()); i++) {
            result += arr.get(i);
        }
        return result;
    }
}

