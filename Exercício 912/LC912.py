class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def heapify(heap_size: int, root: int) -> None:

            largest = root
            left  = 2 * root + 1
            right = 2 * root + 2

            # Se o filho da esquerda for maior que o pai
            if left < heap_size and nums[left] > nums[largest]:
                largest = left

            # Se o filho da direita for maior que o maior até agora
            if right < heap_size and nums[right] > nums[largest]:
                largest = right

            # Se o maior mudou, troca e continua heapify recursivamente
            if largest != root:
                nums[root], nums[largest] = nums[largest], nums[root]
                heapify(heap_size, largest)

        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(end, 0)

        return nums
