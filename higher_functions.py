import functools
from functools import reduce
def run():
    palindrome= lambda x: x == x[::-1]
    print(palindrome('ana'))
    my_list=[1,2,5,6,9,19]
    even=list(filter(lambda x : x%2 == 0, my_list))
    squares =list(map(lambda x : x**2, my_list))
    all_multiplied= (reduce(lambda a,b:a*b, my_list))
    print(f'lista ={my_list}')
    print(f'filter ={even}')
    print(f'map = {squares}')
    print(f'reduce= {all_multiplied}')
if __name__=="__main__":
    run()