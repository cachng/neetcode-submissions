class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []

        buckets = [[] for _ in range(len(nums) + 1)]
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        for key in d:
            buckets[d[key]].append(key)

        for i in range(len(buckets) - 1, 0, -1):
            ans.extend(buckets[i])
            if len(ans) == k:
                return ans

        return ans