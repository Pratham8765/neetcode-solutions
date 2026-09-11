class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map={}
        for n in nums:
            if n in count_map:
                count_map[n]+=1
            else:
                count_map[n]=1
        buckets=[[]for _ in range(len(nums)+1)] 

        for num,count in count_map.items():
            buckets[count].append(num)
        res=[]

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res

