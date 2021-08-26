k = 11
nums = [1,2,3,5,6,4,7,8,9,11,15,28,0]

def findpair(list1, k):
    for i in range(0, len(list1)):
        for j in range(0, len(list1)):
            if k == list1[i] + list1[j]:
                return True    
    return False       
print(findpair(nums, k))

