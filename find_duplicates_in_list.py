class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_length = len(nums)

        nums_length = len(nums)

        seen_set = set()
        duplicate_element = [x for x in nums if x in seen_set or (seen_set.add(x) or False)]

        print(duplicate_element)

        if len(duplicate_element) != 0:
            return True
        else:
            return False

        # # iterates over all indexes
        # for i in range(nums_length):
        #     k = i + 1
        #     for j in range(k, len(nums), 1):
        #         if nums[i] == nums[j]:
        #             return True
        #
        # return False


solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4]))
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))