# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly 
# ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
# 
# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

##
#Codewars problem
#This solution loops through the array and solves concurrently, not using the count() method because that increases runtime.
##

def isValidWalk(walk):
    #determine if walk is valid
    n = 0
    s = 0
    e = 0
    w = 0
    for count,dir in enumerate(walk):
        if(len(walk) < 10 or len(walk) > 10):
            return False
        if(dir == 'n'):
            n += 1
        if(dir == 's'):
            s +=1
        if(dir == 'e'):
            e +=1
        if(dir == 'w'):
            w += 1

    if (((n - s) == 0) and ((w - e) == 0)):
        return True
    else:
        return False
        
        
for i in range(2): # test as many times as you want, just change the number
    test1 = create_tests(random.randint(0,20))
    test.assert_equals(isValidWalk(test1[0]),test1[1])
