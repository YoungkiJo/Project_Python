import collections


a = "A man, a plan, a canal: Panama"
b = "race a car"

""" 리스트 기반 펠린드롬"""
def isPalindromel(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

print(isPalindromel(b))

""" 데크 기반 펠린드롬"""

def isPalindromed(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

print(isPalindromed(a))
