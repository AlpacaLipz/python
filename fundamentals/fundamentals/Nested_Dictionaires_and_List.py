# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1 cahnge the value in x from 10 to 15
x[1][0] = 15

# change the last_name of the first student from jordan to bryant
students[0] ['last_name'] = 'bryant'

# in sports directory change messi to andres

# sports_directory['soccer'][0]= 'Andres'

# change the value from 20 to 30 in variable z

# z[0]['y'] = 30
# print(z)

# iterate through a list of dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# pass a list into the function
# create a for loop to get each indivdual dictionary

def iterate_dictionary(some_list):
    for dictionary in some_list:
        # print(dictionary)
        for key, val in dictionary.items():
            print(f"{key} - {val} ")

iterate_dictionary(students)

# Get values from a list of dictionaries
# create a function 

def iterate_dictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])
    
iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)


dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(some_dict):
    for info in some_dict:
        print(f"{len(some_dict[info])} {info.upper()}")
        for val in some_dict[info]:
            print(val)
        
print_info(dojo)

        # print_info()
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)