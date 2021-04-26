chuoi = input()
i = 0
start = 0
maxLen = 1
while i < len(chuoi):
    left = i
    right = i
    while right < len(chuoi) - 1 and chuoi[right + 1] == chuoi[right]:
        right+=1
    i = right
    while left >= 0 and right < len(chuoi) - 1 and chuoi[right + 1] == chuoi[left - 1]:
        left -= 1
        right += 1
    if left < 0 or right == len(chuoi):
        left += 1
        right -= 1
    newLen = len(chuoi[left:right + 1])
    if newLen > maxLen:
        start = left
        maxLen = newLen        
    i+=1
print(chuoi[start:start+maxLen])