vector<int> result;
for (auto value : values) {
    if (boost::any_cast<int>(value)) {
        result.push_back(boost::any_cast<int>(value));
    }
}

