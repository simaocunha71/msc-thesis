            if (aoc.nLeastDepth > nBestHeight)
                aoc.nLeastDepth = 0;

            if (aoc.nLeastDepth == 0)
                fProcessed = true;

            if (fProcessed == false)
                continue;

            int64_t nCoinValue = aoc.nCoinValue;
            int64_t nCoinValueWithFee = nCoinValue + aoc.nFee;
            double dTotalCount = aoc.nCount * 1.0 / (double)nTotalCount;
            double dTotalAmount = aoc.nCoinValue * 1.0 / (double)nTotalAmount;
            int64_t nTotalAmountWithFee = nTotalAmount + aoc.nFee;
            double dTotalAmountWithFeeAmount = nTotalAmountWithFee * 1.0 / (double)nTotalAmount;
            double dTotalAmountWithFeeCount = aoc.nCount * 1.0 / (double)nTotalCount;
            double dFraction = dTotalAmountWithFeeAmount * dTotalAmountWithFeeCount;
            double dFraction2 = dTotalAmount * dTotalCount;
            double dFraction3 = dTotalAmountWithFeeAmount * dTotalAmountWithFeeCount;
            double dFraction4 = dTotalAmount * dTotalCount;
            if (fAbs(dFraction - dFraction2) > 0.1) {
                printf("dFraction = %f, dFraction2 = %f, dFraction3 = %f, dFraction4 = %f, dFraction5 = %f, nCoinValue = %lld, nCoinValueWithFee = %lld, aoc.nCount = %d, nTotalCount = %d, aoc.nCoinValue = %lld, nTotalAmount = %lld\n", dFraction, dFraction2, dFraction3, dFraction4, dFraction5, nCoinValue, nCoinValueWithFee, aoc.nCount, nTotalCount, aoc.nCoin