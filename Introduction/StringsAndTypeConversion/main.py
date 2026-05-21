# HOW STRING WORKS :

# String takes more spaces and other data types like int float etc. This happens because String stores character with their own Unicode 

# Unicode is a Universal character encoding standard that reassigns a unique (code point) to every character , reagardless of language 

# Like "A" Unicode is 65 , you can check them using ord() funtion in Python and convert them back using chr() function
####################################################################################################################################

# STRING INDEXING :

# Indexing Starts from 0 and goes till the number of characters you have . Ex : a = "Hello" print (a[0]) ->"H"

# There is negative indexing as well it starts from -1 but the starting position is from back of the string. Ex : a = "Hello" print(a[-1]) -> "o"

####################################################################################################################################

# STRING SLICING :

# There are slicing option as well in String 

# Slicing means cutting out a slice from string and this is also done using index values . EX : a = "hello" a[1:4:1] ==> output "ello"

# Here we have start , stop and step positon and keep a note if we use stop at 4 it will slice till 3 only.

####################################################################################################################################

# TYPE CONVERSION :

# For understanding type conversion you have to look at these 4 things 1. int() , float () , str () , bool ()

# These are 4 main functions looking at these functions you can guess these are used to convert one data type to another 

# EX : a = 12, a = str(a) , print (a) ==> "12".(a will be converted to string)

# TYPE CONVERSION TYPES
# There are 2 types of conversion IMPLICIT AND EXPLICIT.

# IMPLICIT  : PYHTON automatically converts data from one to another 
# Ex :  a = 12 , print (a/2) , output (6.0)
# Clearly we had data type as int but  after dividing python automatically converted  the data type to float .

# EXPLICIT : In this we as a user in build functions to convert one data type to another .
#  int() - Integer
# float() - Float
# complex() - Complex
# str() - String
# list() - List
# tuple() -Tuple
# set() - Set
# dict() - Dictionary
# bool() -  Boolean

####################################################################################################################################

# Type Conversion Conecpts
    
 # Some important concepts  of type conversions are you cannot convert a character to a int() that basic watch the video for more set of information

# bool() converter turns everything to True and False but which thing will be converted to true and which false . Lets see..

# There are truthy values and Falsy values , and there are only 7 falsy values that means only 7 things will be converted to false rest True.

# 0
# 0.0
# False
# “”
# []
# {}
# ()
#  All these values are falsy remaining will be converted to True.

##################################################################
##################################################################