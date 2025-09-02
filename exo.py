import re
i=1
while i<100:
    response = ""
    has_3 = re.search("3", str(i))
    has_5 = re.search("5", str(i))
    if has_3:
        response += "Fizz"
    if has_5:
        response += "Buzz"
    if i%3==0:
        response += "Fizz"
    if i%5==0:
        response += "Buzz"
    if has_3 is None and has_5 is None and i%3 != 0 and i%5 != 0:
        response += str(i)
    print(response)
    i+=1