def maximum(list):
    # Returns the maximum value in a list of integers/floats.
    # We firstly assign the maximum value to be the 1st one.
    # Note how we do not name it max!
    n = len(list)
    max_value = list[0]
    # We compare the value of each element of the list to the 1st one,
    # reassigning the maximum value if a larger value exists.
    for i in range(n):
        if max_value < list[i]:
            max_value = list[i]
    return max_value


def minimum(list):
    # Returns the minimum value in a list of integers/floats.
    # We firstly assign the minimum value to be the 1st one.
    # Note how we do not name it min!
    n = len(list)
    min_value = list[0]
    # We compare the value of each element of the list to the 1st one,
    # reassigning the minimum value if a smaller value exists.
    for i in range(n):
        if min_value > list[i]:
            min_value = list[i]
    return min_value


user_list = []
# We let the user insert values over an infinite loop, which can
# only be stopped when the user prompts it to.
while True:
    add_list = int(input("Enter a new integer into our array. "))
    user_list.append(add_list)
    user_action = input("Stop the process? Input stop to stop the process. ")
    if user_action.lower() == "stop":
        break
# We create a new list for the maximum and minimum values of user_list.
# We use our own definition of maximum and minimum for lists.
result_list = []
result_list.append(minimum(user_list))
result_list.append(maximum(user_list))
print(result_list)
