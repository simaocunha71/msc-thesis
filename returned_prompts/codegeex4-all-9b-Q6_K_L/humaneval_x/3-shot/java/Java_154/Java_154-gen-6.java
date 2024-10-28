        return a.contains(b) || a.contains(new StringBuilder(b).append(b).substring(1));
    }
}

