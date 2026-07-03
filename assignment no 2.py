#part A python list (10  questions biggener)

#Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.
list_nums=[3,1,4,1,5]
print("First element=", list_nums[0])
print("Last element=", list_nums[-1])

#Find the length of the list colors = ['red', 'blue', 'green'].
list_colors=['red','blue','green']
print("List colors=", list_colors)
print("Length of the list colors=", len(list_colors))

#Append 'yellow' to the list colors = ['red', 'blue'].

add_item_list=['red','blue']
print("add_item_list")
add_item_list.append('yellow')
print("after append item=",add_item_list)

#insert'orange' at index 1 in fruits=[apple,banana]

insert_item_list=[apple,banana]
print("insert_item_list")
insert_item_list.insert(1,'orange')
print("after insert item=",insert_item_list)

#remove'banana' form fruits=[apple,banana,grapes]

remove_item_list=[apple,banana,grapes]
print("remove_insert_list")
remove_item_list.remove('banana')
print("after removing item=",remove_item_list)

#pop the lats element from items=[10,20,30] and print the popped value.
items=[10,20,30]
print("items")
items.pop(1)
print("after poped the item=",items) 

#check if 3 is in the list nums=[1,2,3,4]
nums=[1,2,3,4]
print("nums")
if 3 in nums:
    print("3 is in the list")
else:
   print("3 is not in the list")

#print the slice [2,3] from the list [0,1,2,3,4]

slice_list=[0,1,2,3,4]
print("slice_list")
print("sub value of given value=",slice_list[2:4])

# replace the element at index 1 in a=[5,10,15] with 12
a=[5,10,15]
print("a")
a[1]=12
print("after replacing the element at index 1=",a)

#Count how many times 2 appears in [1, 2, 2, 3, 2].

for_count=[1,2,2,3,2]
print("for_count")
totall=for_count.count(2)
print("total count of 2 in the list=",totall)

# create B PYTHON TUPLE(10 QUESTION BEGINNER)

#Create a tuple t = (10, 20, 30) and print the second element.

tuple_t=(10,20,30)
print("tuple_t")
print("second element of tuple=",tuple_t[1])

# find the length of the tuple('a','b','c')

find_length=("a","b","c")
print("find_length")
print("length of the tuple=",len(find_length))

# unpack the tuple=(4,5) into variables x and y
#tip:x,y=(4,5)

x,y=(4,5)
print("value of x=",x)
print("value of y=",y)

# check if 'b' is in the tuple ('a','b','c').

check_tuple=('a','b','c')
print("check_tuple")
if 'b' in check_tuple:
    print("b is in the tuple")
else:
    print("b is not in the tuple")

# crate a empty tuple and print it.
empty_tuple=()
print( type(empty_tuple))

#Concatenate (1, 2) and (3, 4) into a new tuple.

tuple1=(1,2)
tuple2=(3,4)
tuple3=tuple1+tuple2
print("after ading two tuple=",tuple3)

#Repeat (7,) three times.

repeat_tuple=(7,)
result=repeat_tuple*3
print("after repeating the tuple three times=",result)

#Find the index of 2 in (1, 2, 3, 2).

index_tuple=(1,2,3,2)
print("index_tuple")
position=index_tuple.index(2)
print("index of 2 in the tuple=",position)

#Count how many times 2 appears in (1, 2, 3, 2).

count_tuple=(1,2,3,2)
print("count_tuple")
results=count_tuple.count(2)
print("total count of 2 in the tuple=",results)

#Create a single‑ element tuple containing the value 5.
#Tip: Remember to use a comma: (5,).

single_tuple=(5,)
print("single_tuple")
print(type(single_tuple))
print("next.....")

#2nd method 

single_tuple2 = (5,)
print(single_tuple2)
print(type(single_tuple2))

# add element 2 from the set{1,2,3}

add_set={1,2,3}
print("add_set")
add_set.add(2)
print("after adding element 2 in the set=",add_set)

# remove element 3 from the set{1,2,3}
remove_set={1,2,3}
print("remove_set")
remove_set.remove(3)
print("after remove element 3 in the set=",remove_set)

#Check if 5 is in the set {1, 3, 5}.

check_set={1,2,3,5}
print("check_set")
if 5 in check_set:
    print("5 is in the set")
else:
    print("5 is not in the set")

#Find the length of set {10, 20, 30}.

length_set={10, 20, 30}
print("length_set")
print("length of the set=",len(length_set))

#Clear all elements from the set {1, 2, 3}.

clear_set={1,2,3}
print("clear_set")
clear_set.clear()
print("after clearing all elements from the set=",clear_set)


#Create a set {'a', 'b'} and add 'c' only if it’s missing.
#Tip: Check membership first: if 'c' not in s:.

create_set={'a','b'}
print("create_set")
if 'c' not in create_set:
    create_set.add('c')
print("after adding 'c' if it was missing=",create_set)


#Convert list ['a', 'a', 'b'] into a set to remove duplicates.
#Tip: Casting removes duplicates automatically.

convert_list=['a', 'a', 'b']
print("convert_list")
converted_set=set(convert_list)
print("after converting list to set=",converted_set)

#Create two sets and print their union.
#Tip: Use set1 | set2.

set1={1,2,3}
set2={3,4,5}
union_set=set1 | set2
print("union of set1 and set2=",union_set)

#Create two sets and print their intersection.
#Tip: Use set1 & set2.

setno1={1,2,3}
setno2={2,3,4}
intersection_set=setno1 & setno2
print("intersection of setno1 and setno2=",intersection_set)

#Part D — Python Dictionaries (10 Beginner Questions)

#Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
#Tip: Use d['name'].

new_dict={'name':'ali','age':25}
print("new_dict")
print("Name is here :",new_dict["name"])

#Add key 'city': 'Lahore' to a dictionary.
#Tip: Use assignment: d['city'] = 'Lahore'.

Add_dict={"age":25}
print(Add_dict)
Add_dict["City"]="lahore"
print("after addition =",Add_dict)

#Change 'age' in {'name': 'Ali', 'age': 25} to 30.
#Tip: Assign a new value: d['age'] = 30.

change_dict={'name':'ali','age':25}
print("change_dict")
change_dict['age'] = 30
print("after changing age =",change_dict)

#Delete key 'age' from a dictionary.
#Tip: Use del d['age'].

delete_dict={'name':'ali','age':25}
print("delete_dict")
delete_dict['age']
print("after delete age=",delete_dict)

#Check if key 'salary' exists in a dictionary.
#Tip: Use in operator.

check_dict={'salary':5000,'age':25}
print("check_dict")
if 'salary' in check_dict:
    print("salary is in the dictionary")
else:
    print("salary is not in the dictionary")

#Print all keys from {'a': 1, 'b': 2}.
#Tip: Use d.keys().

my_dict={'a':1,'b':2}
print("my_dict")
print("Keys in the dictionary:", list(my_dict.keys()))

#Print all values from a dictionary.
#Tip: Use d.values().

your_dict={'w':7,'q':2,'f':1}
print("your_dict")
print("value is here=",your_dict)

#Iterate and print key‑ value pairs from {'x': 10, 'y': 20}.
#Tip: Use for k, v in d.items().

hlo_dict={'x':10,'y':20}
print("hlo_dict")
for k, v in hlo_dict.items():
    print(f"Key: {k}, Value: {v}")

#Use get() to safely read key 'score' from an empty dictionary.
#Tip: Use d.get('score', default_value).

game_data={}
current_score=game_data.get(score,0)
print("current_score")

#Create a dictionary from two lists: keys = ['a','b'], values = [1,2].
#Tip: Use dict(zip(keys, values)).

keys={'a','b'}
values={1,2}
dict=dict(zip(keys,values))
print("dict")

