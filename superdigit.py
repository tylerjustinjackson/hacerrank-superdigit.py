#!/bin/python3

#super digit main function
def super_digit(n, k):

    #makes all the number integer from n list
    digits = map(int, list(n))
    
    #calls get super digit secondary function and
    #passes the digits to the function
    return get_super_digit(str(sum(digits) * k))

#define get super digit function
def get_super_digit(p):

    #finds lenght of p and sees if it is 1
    if len(p) == 1:

        #returns p if length is 1
        return int(p)

    #otherwise maps all digits back into integers
    #and restarts process
    else:
        digits = map(int, list(p))
        return get_super_digit(str(sum(digits)))

if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = super_digit(n, k)
    print(result)
