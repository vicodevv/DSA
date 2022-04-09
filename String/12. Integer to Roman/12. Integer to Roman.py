class Solution:
    def intToRoman(self, num: int) -> str:
        integer = [[1, "I"], [4, "IV"], [5, "V"], [9, "IX"],[10, "X"],[40, "XL"],[50, "L"],[90, "XC"],[100, "C"],[400, "CD"],[500, "D"],[900, "CM"],[1000, "M"]]
        result = ""
        
        for val, rom in reversed(integer):
            if num // val:
                count = num // val
                result += (rom * count)
                num = num % val
        return result