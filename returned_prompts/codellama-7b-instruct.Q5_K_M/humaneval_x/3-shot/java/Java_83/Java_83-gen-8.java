        int result = 0;
        for (int i = 1; i <= n; i++) {
            String current = Integer.toString(i);
            if (current.startsWith("1") || current.endsWith("1")) result += 1;
        }
        return result;
    }
}

