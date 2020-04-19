# https://leetcode.com/problems/integer-to-roman/
def intToRoman(self, num: int) -> str:
        if num >= 4000:
            print("Unsupported num")
            return ""
        
        roman = ''
        D = dict(zip([0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900],                                    ['','I','II','III','IV','V','VI','VII','VIII','IX','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'])) #zip creates a dictionary from these 2 arrays
        print(D)

        thousands = num // 1000
        hundreds = (num % 1000) // 100
        tens = ((num % 1000) % 100) // 10
        ones = ((num % 1000) % 100) % 10

        roman += thousands *'M'
        roman += D[hundreds * 100]
        roman += D[tens * 10]
        roman += D[ones]
        return roman

'''
given 2 dates (return, due)
return == due -> $0 fine
return >= due + 1 month -> $500/month and $15/day
return >= due + 1 year -> $10,000
'''

def get_fine(d1, m1, y1, d2, m2, y2): #1 is return, 2 is due
    #check if years are the same
    if y1 > y2:
        return 10000
    #check the month
    if m1 > m2 and y1 == y2:
        return (m1 - m2) * 500
    #check the day
    if d1 > d2 and m1 == m2 and y1 == y2:
        return (d1 - d2) * 15
    return 0

print(get_fine(2, 7, 1014, 1, 1, 1015))

