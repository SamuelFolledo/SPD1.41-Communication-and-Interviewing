
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