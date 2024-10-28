 // adjust least depth to best height
            for (std::vector<COutput>.iterator oi = anonOutputList.begin(); oi != anonOutputList.end(); ++oi)
            {
                COutput& output = *oi;
                // Check if the output is processed
                if (output.nHeight <= nBestHeight && output.nHeight >= aoc.nLeastDepth)
                {
                    // Check if the output is in the map
                    if (mapAnonOutputStats.find(output.GetHash()) != mapAnonOutputStats.end())
                    {
                        CAnonOutputCount& aoc2 = mapAnonOutputStats[output.GetHash()];
                        aoc2.nCount++;
                        fProcessed = true;
                    }
                }
            }
            if (!fProcessed)
            {
                mapAnonOutputStats.erase(mi);
            }
        }
        // ... more code ...


Here is the code so far:

```cpp
if (!mapAnonOutputStats.empty())
{
    throw std::runtime_error("CountAllAnonOutputs() failed.");
}
```

I will add the next few lines of code. Here they are:

```cpp
else
{
    // TODO: make mapAnonOutputStats a vector preinitialised with all possible coin values?
    for (std::map<int64_t, CAnonOutputCount>::iterator mi = mapAnonOutputStats.begin(); mi != mapAnonOutputStats.end(); ++mi)
```

Let me know if you'd like me to add more lines of code. Just let me know what you'd like me to add. I can add a few more lines to help with the problem you're trying to solve. Just let me know what you need help with.