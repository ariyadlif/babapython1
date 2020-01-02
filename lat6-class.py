# class MyClass:
# 	nama = "Babastudio"

# p1 = MyClass()
# print(p1.nama)

# =======================

# class Person:
# 	def __init__(obj, name, age):
# 		obj.name = name
# 		obj.age = age

# 	p1 = Person("John", 36)

# 	print(p1.name)
# 	print(p1.age)

# =========================

class Person:
	def __init__(obj, name, age):
		obj.name = name
		obj.age = age

	def myfunc(abc):
	print("Hello my name is" + abc.name)
	print("My age is " + str(abc.age))

p1 = Person("John", 35)
p1.myfunc()