        return (x instanceof Integer && y instanceof Integer && z instanceof Integer) &&
                ((int) x + (int) y == (int) z || (int) y + (int) z == (int) x || (int) x + (int) z == (int) y);
    }
}

