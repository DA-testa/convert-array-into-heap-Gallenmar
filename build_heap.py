# python3
import math

def build_heap(a,n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    lastNonLeafIndx = math.ceil((n/2)-1)
    for i in reversed(range(1,lastNonLeafIndx+1)):
        j = i
        # print(i)
        # print(j)
        flag = True
        while flag:
            l=j*2
            r=j*2+1
            if (l>n)or(r>n):
                flag=False
                continue
            if (a[j-1]>a[l-1]) or (a[j-1]>a[l-1]):
                if (a[l-1]<a[r-1]):
                    swaps.append((j-1,l-1))
                    tmp = a[l-1]
                    a[l-1] = a[j-1]
                    a[j-1] = tmp
                    j=l
                elif (a[l-1]>a[r-1]):
                    swaps.append((j-1,r-1))
                    tmp = a[r-1]
                    a[r-1] = a[j-1]
                    a[j-1] = tmp
                    j=r
                else:
                    flag = False
                    # it shouldnt reach this part of code
            else:
                    flag = False

        # l=i*2
        # r=i*2+1
        # if (a[l-1]<a[r-1]):
        #     if (a[l-1]<a[i-1]):
        #         j=i
        #         while not flag:
        #             l=j*2
        #             r=j*2+1
        #             tmp = a[l-1]
        #             a[l-1] = a[i-1]
        #             a[i-1] = tmp
        #             if (a)
        # else:
        #     if (a[r-1]<a[i-1]):
        #         tmp = a[r-1]
        #         a[r-1] = a[i-1]
        #         a[i-1] = tmp
    


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input()
    if 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in text:
        name = input()
        if not 'a' in name: 
            name = "tests/"+name
            f = open(name, "r")
            n = int(f.readline())
            data = list(map(int,f.readline().split()))
    assert len(data) == n


    # input from keyboard
    # n = int(input())
    # data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    # assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data,n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
