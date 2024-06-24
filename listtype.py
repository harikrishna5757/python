list_variable = ["w", "date", "bdd", "test"]
list_variable.append("news")
print(list_variable)

list_variable.insert(2, "data")
print(list_variable)

list_variable.remove("date")
print(list_variable)

print(max(list_variable))
print(min(list_variable))
print(sorted(list_variable))

list_variable.sort(reverse=True)
print(list_variable)
