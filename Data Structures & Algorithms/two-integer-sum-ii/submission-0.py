class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = defaultdict(int)

        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem in complement:
                return [complement[rem] + 1,i + 1 ]

            complement[numbers[i]] = i
        return -1