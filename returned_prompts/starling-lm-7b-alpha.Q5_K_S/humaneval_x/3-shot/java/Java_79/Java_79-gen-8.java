        String binary = "db";
        for (int i = 0; i < 8; i++) {
            binary += (decimal & (1 << i)) > 0 ? '1' : '0';
        }
        return binary + "db";
    }
}

