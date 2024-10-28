
            if (aoc.nLargestDepth > 0)
                aoc.nLargestDepth = nBestHeight - aoc.nLargestDepth;
            for (std::map<int64_t, CAnonOutputCount>::iterator mi = mapAnonOutputStats.begin(); mi != mapAnonOutputStats.end(); ++mi)
            {
                CAnonOutputCount &aoc2 = mi->second;
                if (aoc2.nLeastDepth > aoc.nLeastDepth)
                    aoc.nLeastDepth = aoc2.nLeastDepth;
                if (aoc2.nLargestDepth < aoc.nLargestDepth)
                    aoc.nLargestDepth = aoc2.nLargestDepth;
            }
            if (aoc.nLargestDepth > 0)
                aoc.nLargestDepth = nBestHeight - aoc.nLargestDepth;
            if (aoc.nLeastDepth > 0)
                aoc.nLeastDepth = nBestHeight - aoc.nLeastDepth;
            if (aoc.nLargestDepth > nAnonOutputDepth)
                aoc.nLargestDepth = nAnonOutputDepth;
            if (aoc.nLeastDepth < nAnonOutputDepth)
                aoc.nLeastDepth = nAnonOutputDepth;
            if (aoc.nLargestDepth > 0 && aoc.nLargestDepth < nAnonOutputDepth)
            {
                if (!fProcessed)
                {
                    fProcessed = true;
                    CAnonOutputCount &aoc2 = mapAnonOutputStats[aoc.nValue];
                    aoc2.nLargestDepth = aoc.nLargestDepth;
                    aoc2.nLeastDepth = aoc.nLeastDepth;
                    aoc2.nCount += aoc.nCount;
                }
