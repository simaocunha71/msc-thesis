        for (Object k: dict.keySet()) {
            if (!(k instanceof String)) continue A;
            if (!((String)k).toLowerCase().equals((String)k)) continue A;
        }

        return true;
    }
}
