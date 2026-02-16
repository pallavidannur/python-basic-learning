birthday = {
    "pallavi": "03-08-2006",
    "sneha": "12-09-2005",
    "priya": "25-11-2006"
}

meanings ={
    "bat":"used to hit",
    "ball":"this is hit",
    "wicket":"to be protected"
}

print(birthday["pallavi"])
print(birthday["sneha"])
print(birthday["priya"])        
print(birthday.get("pallavi"))
print(birthday.get("sneha"))
print(birthday.get("priya"))   
print(birthday.get("sudeep")) 

print(birthday)
print("adding suddep to the list")
birthday["sudeep"] = "02-09-1973" 
print(birthday)

print(birthday)
print("updating...")
birthday["pallavi"] = "03-08-2007"
print(birthday) 
birthday.pop("sudeep")
print(birthday)


print(birthday.keys())
print(birthday.values())

print(birthday.items())
