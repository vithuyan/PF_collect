# Exercise 9
grocery_list = ["carrots", "toilet paper", "apples", "salmon", "rice"]
def list_item(list):
    for grocery in grocery_list:
        print('*{}'.format(grocery))
print(list_item(grocery_list))
print (len(grocery_list))

if "bananas" in grocery_list:
    print('we have bananas.')
else:
    print('we need bananas')

print ('grocery_list [1]')

grocery_list.sort()
print(list_item(grocery_list))

grocery_list.pop(3)
print(list_item(grocery_list))
