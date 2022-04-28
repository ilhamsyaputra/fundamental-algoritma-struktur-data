def two_sum(nums: list[int], target: int) -> list[int]:
    hash_map = {}

    for index, value in enumerate(nums):
        second_element = target - value

        if second_element in hash_map:
            return [hash_map[second_element], index]
        
        hash_map[value] = index