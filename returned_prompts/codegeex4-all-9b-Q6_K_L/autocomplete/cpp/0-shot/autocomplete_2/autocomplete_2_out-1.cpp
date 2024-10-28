            if (aoc.nLeastDepth > 0)
                aoc.nLeastDepth = nBestHeight - aoc.nLeastDepth;
            if (aoc.nMostDepth == 0)
                aoc.nMostDepth = nBestHeight;
            if (aoc.nMostDepth > 0 && aoc.nLeastDepth > 0)
                aoc.nDepthRange = aoc.nMostDepth - aoc.nLeastDepth;
            if (aoc.nMostDepth > 0 && aoc.nDepthRange > 0)
                aoc.nDepthPerTx = aoc.nDepthRange / aoc.nMostDepth;
            if (aoc.nLeastDepth > 0 && aoc.nDepthPerTx > 0)
                aoc.nDepthPerTx = aoc.nDepthRange / aoc.nLeastDepth;
            if (aoc.nDepthPerTx > 0)
                aoc.nDepthPerTx = 1;
            if (aoc.nMostDepth > 0)
                aoc.nMostDepth = 1;
            if (aoc.nLeastDepth > 0)
                aoc.nLeastDepth = 1;
            if (aoc.nDepthRange > 0)
                aoc.nDepthRange = 1;
            if (aoc.nDepthPerTx > 0)
                aoc.nDepthPerTx = 1;
            if (aoc.nMostDepth > 0)
                aoc.nMostDepth = 1;
            if (aoc.nLeastDepth > 0)
                aoc.nLeastDepth = 1;
            if (aoc.nDepthRange > 0)
                aoc.nDepthRange = 1;
            if (aoc.nDepthPerTx > 0)
                aoc.nDepthPerTx = 1;
            if (aoc.nMostDepth > 0)
                aoc.nMostDepth = 1;
            if (aoc.nLeastDepth > 0)
                aoc.nLeastDepth = 1;
            if (aoc.nDepthRange > 0)
                aoc.nDepthRange = 1;
            if (aoc.nDepthPerTx > 0)
                aoc.nDepthPerTx = 1;
            if (aoc.nMostDepth > 0)
                aoc.nMostDepth = 1;
            if (aoc.nLeastDepth > 0)
                aoc.nLeastDepth = 1