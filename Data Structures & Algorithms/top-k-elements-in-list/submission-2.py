from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        sorted_items = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [num for num, count in sorted_items[:k]]