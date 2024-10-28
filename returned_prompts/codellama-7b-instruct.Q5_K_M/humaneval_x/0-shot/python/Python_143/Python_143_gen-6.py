
class Solution:
    def words_in_sentence(self, sentence: str) -> str:
        return ' '.join(word for word in sentence.split() if self.is_prime(len(word)))

    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
