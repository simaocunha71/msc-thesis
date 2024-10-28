            for (std::map<int64_t, CAnonOutputCount>::iterator mi = mapAnonOutputStats.begin(); mi != mapAnonOutputStats.end(); ++mi)
            {
                if (fProcessed || mi->second.nLeastDepth != aoc.nLeastDepth || mi->second.nCoins > 0)
                    continue;
mi->second.nCoins = aoc.nCoins;
                mi->second.nDenom = aoc.nDenom;
                mi->second.nLeastDepth = aoc.nLeastDepth;
                fProcessed = true;
            }
            if (!fProcessed)
            {
                CAnonOutputCount aoc(aoc.nCoins, aoc.nDenom, aoc.nLeastDepth);
                mapAnonOutputStats.insert(std::make_pair(aoc.nDenom, aoc));
            }
        }
    }

