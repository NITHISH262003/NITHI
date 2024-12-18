def closest_number(nums):
    a=0
    closest = nums[0]
    min_distance = abs(nums[0] - a)
    
    for num in nums[1:]:
        distance = abs(num - a)
        if distance < min_distance or (distance == min_distance and num > closest):
            closest = num
            min_distance = distance
    return closest
nums=[-1,-2,1]
print(closest_number(nums))
 print("hello world")
print("tomorrow holiday")
