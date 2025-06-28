class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def merge_sort(lo, hi):
        
            if lo >= hi:
                return 0

            mid = (lo + hi) // 2
            
            count = merge_sort(lo, mid) + merge_sort(mid + 1, hi)

            # Conta pares cruzados (i na esquerda, j na direita)
            j = mid + 1
            for i in range(lo, mid + 1):
                while j <= hi and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge clássico para ordenar nums[lo..hi]
            temp = []
            left, right = lo, mid + 1
            while left <= mid and right <= hi:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            # Anexa restos
            temp.extend(nums[left: mid + 1])
            temp.extend(nums[right: hi + 1])
            nums[lo: hi + 1] = temp

            return count

        return merge_sort(0, len(nums) - 1)
