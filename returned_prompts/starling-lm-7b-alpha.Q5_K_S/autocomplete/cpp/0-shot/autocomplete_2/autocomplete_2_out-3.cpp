
            if (aoc.nLeastDepth < 0)
                aoc.nLeastDepth = 0;

            for (int64_t nCoin = aoc.nCoin; nCoin > 0 && !fProcessed; nCoin /= 2)
            {
                if (!mapAnonOutputStats.count(nCoin))
                    mapAnonOutputStats[nCoin] = CAnonOutputCount();
                CAnonOutputCount& aoc2 = mapAnonOutputStats[nCoin];

                if (nCoin == aoc.nCoin)
                {
                    int64_t nTarget = aoc.nCoin * 2;
                    if (nTarget > aoc2.nCoin)
                        nTarget = aoc2.nCoin;
                    while (nTarget > 0 && aoc.nLeastDepth >= aoc2.nLeastDepth)
                    {
                        // Find a coin value that can be doubled to reach a target value that is >= aoc2's least depth.
                        if (nTarget > aoc2.nCoin)
                            nTarget = aoc2.nCoin;
                        if (nTarget > aoc.nCoin)
                            nTarget = aoc.nCoin;
                        if (nTarget > 0 && aoc.nLeastDepth >= aoc2.nLeastDepth)
                        {
                            aoc.nCoin = nTarget;
                            aoc.nLeastDepth = std::min(aoc.nLeastDepth, aoc2.nLeastDepth);
                            fProcessed = true;
                            break;
                        }
                        nTarget /= 2;
                    }
                }
            }
            if (!fProcessed)
                LogPrint("CountAllAnonOutputs()", "Failed to process coin=%ld, least depth=%ld\n", aoc.nCoin, aoc.nLeastDepth);
        }
    }

Explanation:

This code is part of the