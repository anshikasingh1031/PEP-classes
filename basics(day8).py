#1(.)any one character can come
# import re
# text="cat cot cut"
# result=re.findall("c.t",text)
# print(result)

#2(^)straing of sentence
# import re
# text="hello world"
#  result=bool(re.search("^hello",text))
# result=bool(re.search("^world",text))
# print(result)

#3(&)end of sentence
# import re
# test="hello world"
# result=bool(re.search("world$",test))
# print(result)

#4 (*) 0 or more
# import re
# text="helloo"
# result=re.findall("o*",text)
# print(result)

#5 one or more(+)
# import re
# text="helloo"
# result=re.findall("lo+",text)
# print(result)

#6-(?) 0 or 1
# import re
# text="color colour"
# result=re.findall("colou?r",text)
# print(result)
 

 #7 character set[]
# import re
# text="apple ball cat"
# result=re.findall("[abc]",text)
# print(result)

#8 digits[0-9]
# import re
# text ="my age is 20"
# result=re.findall("[0-9]",text)
# print(result)

#9 [A-Z] capital alphabets
# import re
# text="my name is ANSHIKA"
# result=re.findall("[A-Z]",text)
# print(result)

#10 [a-z] all small alphabets
# import re
# text="my name is ANSHIKA"
# result=re.findall("[a-z]",text)
# print(result)

#11 [A-Za-z] both small and capital 
# import re
# text="my name is ANSHIKA"
# result=re.findall("[A-Za-z]",text)
# print(result)

#12 (\d) only digit
# import re
# text="my age is: 20"
# result=re.findall("\d",text)
# print(result)

#13 (\D) not digitss
# import re
# text="my age is: 20"
# result=re.findall("\D",text)
# print(result)

#14 (\w) only characters
# import re
# text="heloo anshika" 
# result=re.findall("\w",text)
# print(result)

#15 (\W) no charcaters
# import re
# text="anshika 20"
# result=re.findall("\W",text)
# print(result)

#16 (\s) for space
# import re
# text="anshika singh hey"
# result=re.findall("\s",text)
# print(result)

#17 (\S) no space
# import re
# text="anshika singh hello"
# result=re.findall("\S",text)
# print(result)

#18 ({})repetition count
# import re
# text="hey hello heyy"
# result=re.findall("y{2}",text)
# print(result)

#19 ( | )  OR 
# import re
# text="cat,dog,apple"
# result=re.findall("cat|apple",text)
# print(result)

#20 () grouping
# import re
# text="hellooo hello"
# result=re.findall("(llo)?",text)
# print(result)