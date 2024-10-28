        for (int i = 0; i < Math.sqrt(a); i++) {
            int cube = i * i * i;
            if (cube == a) return true;
        }
        return false;
    }
}

