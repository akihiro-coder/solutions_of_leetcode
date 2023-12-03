class Solution:
    def romanToInt(self, s):
        output = 0

        subtraction_symbol_value = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        for char in subtraction_symbol_value:
            if char in s:
                output += subtraction_symbol_value[char]
                s = s.replace(char, '')
        if not s:
            return output
        
        basic_symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for char in s:
            output += basic_symbol_value[char]

        return output


sol = Solution()
s = 'MCMXCIV'
result = sol.romanToInt(s)
print(result)
