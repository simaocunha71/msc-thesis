            aoc.nMostDepth = nBestHeight - aoc.nMostDepth;
            if (aoc.nMostDepth > 0)
                aoc.nMostDepth -= nBestHeight;
            if (aoc.nLeastDepth < 0)
                aoc.nLeastDepth += nBestHeight; // subtract best height if less than zero
            if (aoc.nMostDepth < 0)
                aoc.nMostDepth += nBestHeight; // subtract best height if less than zero
            fProcessed = true;
        }
    }
    return true;
} // CountAllAnonOutputs

