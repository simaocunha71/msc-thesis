 // convert from block height to depth
            if (aoc.nMostDepth > 0)
                aoc.nMostDepth = nBestHeight - aoc.nMostDepth; // convert from block height to depth

            if (aoc.nCount == 1)
            {
                // If only one, we can't compute confidence
                fProcessed = true;
                if (aoc.nLeastDepth == 0 && aoc.nMostDepth == 0)
                {
                    // If in the best height, it's 100% real
                    nConfidence = 1;
                }
                else if (aoc.nLeastDepth == 0)
                {
                    // If it's only in the best height, it's 100% real
                    nConfidence = 1;
                }
                else if (aoc.nMostDepth <= nConfidenceDepth)
                {
                    // If it's in the best height and a few blocks later, it's 100% real
                    nConfidence = 1;
                }
                else
                {
                    // Otherwise, it's 0% real
                    nConfidence = 0;
                }
            }
            else if (aoc.nCount == 2)
            {
                // If two, we can compute confidence
                fProcessed = true;
                if (aoc.nLeastDepth == 0 && aoc.nMostDepth == 0)
                {
                    // If in the best height, it's 100% real
                    nConfidence = 1;
                }
                else if (aoc.nLeastDepth == 1 && aoc.nMostDepth == 1)
                {
                    // If in the best height and one block later, it's 100% real
                    nConfidence = 1;
                }
                else if (aoc.nLeastDepth == 0)
                {
                    // If it's only in the best height, it's 100% real
                    nConfidence = 1;
                }
                else if (aoc.nMostDepth <= nConfidenceDepth)
                {
                    // If it's in the best height and a few blocks later, it's 100% real
                    nConfidence = 1;
                }
                else
                {
                    // Otherwise, it's 0% real
                    nConfidence = 0;
                }
            }
            else if (aoc.nCount == 3)
            {
                // If