# def iq_test(numbers):
#     #print(numbers.index(i))
#
#     #t = numbers.split()#[i for i in numbers if i.isdigit()]
#     conv = [int(i) for i in numbers.split()]
#     print(conv)
#     Odd =[i for i in conv if i%2==0 ]
#     Even =[i for i in conv if i%2!=0 ]
#     print(Odd,Even)
#     if len(Odd)==1:
#         return([conv.index(i)+1 for i in Odd ][0])
#     else: return([conv.index(i)+1 for i in Even][0])
#
#
# numbers = '38 44 48 32 29 38'
# print(iq_test(numbers))


def solve(s):
    p='('
    c=')'
    # print(s.count(p), s.count(c))
    # for i in s:
    #     print(i.count(p),i.count(c))
    #     if (i.count(p)>i.count(c)):
    #         return [i.count(p)-i.count(c) for i in s]
    #     else: return [(i.count(c)-i.count(p)) for i in s
    n=0
    if s[0+n]==p or c==s[-1-n]:
        n+=1
        return n
    else: return n+1



print(solve(")()("))