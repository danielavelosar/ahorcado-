def list_comprenhension():
    nat_numbers=[i for i in range (1,101)]
    nat_numbers_squared=[]
    nat_numbers_squared_2=[i**2 for i in range(1, 101) if i%3 != 0]
    for number in nat_numbers:
        number_squared= number**2
        nat_numbers_squared.append(number_squared)
    print(f'natural={nat_numbers}')
    print(f'squared={nat_numbers_squared}')
    print(f'squared={nat_numbers_squared_2}')

def dict_comprenhension():
    dict_number_cubed={i:i**3 for i in range (1,101) if i%3 !=0}
    for key, value in dict_number_cubed.items():
        print (key, ("-"), value)
def main():
    super_list=[
        {"name":"paula", "last name":"velosa"},
        {"name":"daniela", "last name":"romero"},
        {"name":"edgar", "last name":"duque"},
        {"name":"olga", "last name":"rodriguez"}
    ]
    super_dict={
        "nat_nums":[0,1,2,3],
        "float_nums":[0.2,0.5,0.1]
    }
    
    for key, value in super_dict.items():
        print(key, "-", value)
    
    for dict in super_list:
        for key, value in dict.items():
            print(key, "-", value)

if __name__== "__main__":
    main()
    list_comprenhension()
    dict_comprenhension()