import ipdb 

dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
test_planeteers = ["earth", "wind", "fire", "water", "heart"]

def roll_call_dwarves(dwarves):
    #don't have to do len(dwarves) - 1 because range is exclusive
    #i starts at 1, represents index
    #dwarf represents element
    #enumerate: https://www.geeksforgeeks.org/enumerate-in-python/
    #for i, dwarf in enumerate(dwarves, 1) 
    
    # for i in range(0, len(dwarves)):
    #     print(f"{i+1}. {dwarves[i]}")

    #while we are still in the list
    i = 0
    while(i < len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")
        #HAVE TO UPDATE FOR CONDITIONAL OTHERWISE YOU WILL GET AN INFINITE LOOP
        i = i + 1 

def summon_captain_planet(planeteers):
    # [<replacement value> for <current value> in <list>]
    return [f"{p.capitalize()}!" for p in planeteers]
    # list = []
    # for p in planeteers:
    #     list.append(f"{p.capitalize()}!")
    # return list

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True #return exits the function
    #we've looked at every single word 
    #our for loop is done
    #no words
    return False 
    #return any(len(word) > 4 for word in calls)

def find_the_cheese(foods):
    # list_of_cheese = ["cheddar", "gouda", "camembert"]
    # for food in foods:
    #     if food in list_of_cheese:
    #         return food 
    # return None

    cheesez = ["camembert", "gouda", "cheddar"]
    #default value None, if iterator has reached its end 
    #raises stop iteration exception when it reaches what you are looking for
    #https://www.scaler.com/topics/next-in-python/
    return next((food for food in foods if food in cheesez), None)


# ipdb.set_trace()