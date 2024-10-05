return {
    auto v = values;
    for (auto& it : v) {
        if (it.type() == typeid(int)) {
            it.cast<int>();
        }
    }
    return v;
}

