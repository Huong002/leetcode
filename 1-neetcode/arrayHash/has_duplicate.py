# Cho một mảng số nguyên nums, hàm trả về giá trị truenếu bất kỳ giá trị nào xuất hiện nhiều hơn một lần trong mảng, ngược lại trả về null false.

# Ví dụ 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Ví dụ 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

from typing import List

class Solution:
    # bruce force 
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in  range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False

    # time: O(n)2 , space: O(1)
        
        
    # sorting: sort mang -> kiem  tra i va i++
    def hasDulicateSort(self, nums: List[int]) -> bool:
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] ==  nums[i-1]:
                return True
            
        return False
    # time: Ologn, space O(1) || O(n) : tuy thuat toan sap xep

    
    
    # Hash Set: cho set rong -> duyet mangr-> ko co tong set -> add vao -> co thi ket thuc va tra ve true
    def hasDulicateHashSet(self, nums: List[int])-> bool:
        seen =  set()
        for num  in nums: 
            if num in  seen:
                return True
            seen.add(num)
        return False

        
    #  Hash Set Length: lay do dai set (set la list nhung ko trung) so sanh voi list: neu khac thi  co trung ngyoc lai thi ko trung
    def hasDulicateHashSetLength(self, nums:List[int]) -> bool:
        return len(set(nums)) < len(nums)