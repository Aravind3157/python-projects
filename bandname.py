#this is my first project which covers basics of variables and string concatenation
'''terminology in this code
name_1=string1
name_2= string2
band_name=concatenation of strings
q1,q2=quotient
r1,r2=remainder

'''

name_1 = input("please enter the starting name of band:")
name_2 = input("please enter the ending name of band:")
band_name= name_1 +" "+name_2
print("the band name is :" + band_name)
'''Use the divmod() function to divide the length of the string by 2, which gives us the quotient and remainder. The quotient represents the length of the first part of the string, while the remainder represents the length of the second part of the string. We add the remainder to the quotient to ensure that the first part is longer by one character if the length of the string is odd.
Use string slicing to extract the first and second halves of the string. The [:quotient + remainder] notation means that we want to extract all characters from the beginning of the string up to the end of the first part. The [quotient + remainder:] notation means that we want to extract all characters from the beginning of the second part to the end of the string.
'''
q1,r1=divmod(len(name_1),2)
q2,r2=divmod(len(name_2),2)
updated_name_1=name_1[:q1+r1]
updated_name_2=name_2[q2+r2:]

updated_band_name =updated_name_1 + updated_name_2
print("the updated band name is :" + updated_band_name)