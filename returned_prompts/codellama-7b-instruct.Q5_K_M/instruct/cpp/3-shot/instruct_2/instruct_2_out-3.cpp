        vector<int> depths;
        for (auto it = m.cbegin(); it != m.cend(); ++it)
            depths.push_back(it->second);
        std::sort(depths.begin(), depths.end(), std::greater<int>());

