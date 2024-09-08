    if (base<2||base>9) {
        return "base should be between 2 and 9";
    }
    if (x<base) {
        return to_string(x);
    }
    return change_base(x/base, base)+to_string(x%base);
}

