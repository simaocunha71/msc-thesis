
            else
                aoc.nLeastDepth = nBestHeight;
            if  (aoc.nCoinDay  != -1)
                aoc.nCoinDay  -= nBestHeight  - aof.nCoinDay;
            else
                aoc.nCoinDay  = nBestHeight;
            aoc.nFirstSeen  = std::max(aoc.nFirstSeen,  nBestHeight);
            aoc.nLastSeen   = std::max(aoc.nLastSeen,   nBestHeight);

            // TODO: make the mapAnonOutputStats a vector preinitialised with all possible coin values?
            mapAnonOutputStats[mi->first] = aoc;

            fProcessed  = true;
        }
    }

*/

#include <stdexcept>
#include <map>

int main() {
    throw std::runtime_error("CountAllAnonOutputs() failed.");
}//src/main/cpp/com/github/marcoscalada/crypto/Hash.h
#ifndef CRYPTO_HASH_H
#define CRYPTO_HASH_H

#include <string>

namespace Crypto {
    class Hash {
    public:
        virtual std::string operator()(const std::string &data) const = 0;
    };
}

#endif //CRYPTO_HASH_H

//src/main/cpp/com/github/marcoscalada/crypto/MD5.h
#ifndef CRYPTO_MD5_H
#define CRYPTO_MD5_H

#include "Hash.h"

namespace Crypto {
    class MD5 : public Hash {
    public:
        std::string operator()(const std::string &data) const override;
    };
}

#endif //CRYPTO_MD5_H

//src/main/cpp/com/github/marcoscalada/crypto/SHA1.h
#ifndef CRYPTO_SHA1_H
#define CRYPTO_SHA1_H