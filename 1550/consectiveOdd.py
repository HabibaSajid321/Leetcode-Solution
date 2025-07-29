def consectiveOdd(nums):
    count = 0
    for num in nums:
        if num % 2 == 1:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False
        