# Import randint from random for a random number generator
from random import randint
# Assign the alphabet from a-z in a dict to corrospond from 0-25 - This will be used for index slicing.

index = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18,
"t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
# Each letter will corrospond to the index of list names by alphabetical order
def names():
# There will be a list for each letter & each letter will have an assigned
# number that represents the index in the list of your given letter.

    x = input("Enter the letter you want your baby name to start with: ")
    y = index[x]
# With x we get a input of the letter you want your baby name to start with and identify it in the index dict with y
    myList = [["Albert","Annie","Austin","Andy","Ashley","Anali"], ["Bob","Brent","Brittany","Billy","Boy"],
    ["Chris","Case","Courtney","Catelyn","Carlos"],["Dan","Daustin","Darius","Deyaneira","Daleyza"],
    ["Elisa","Eliza","Ebony","Estaban","Elijah","Eric","Erick","Erica"],["Frank","Fisk","Francis","Franchesca","Fanny"],
    ["Gerald","Greg","George","Girl","Goofy"],["Haley","Hailey","Hannah","Harry","Heith"],["Isaac","Isreal","India","Isaiah","Ira"],["Justin","Juliet","Jalissa","Jose","Jesus","Jessica","Jane"],
    ["Kath","Kala","Kayla","Kyle","Kayel","Kris","King"],["Liz","Lynet","Lyane","Lisa","Liza"],["Malik","Mike","Michael","Michelle","Mya","Mystie"],
    ["Nemo","Nick","Nicholas","Nixon","Nessa"],["Oscar","Omar","Orion","Olivia","Oppa"],["Payne","Paul","Paula","Pamela","Patrick","Patricia"],["Quante","Que"],
    ["Rio","Ryan","Romeo","Richard","Richardson","Ruby","Rabecca","Rose","Rosany"],
    ["Sadie","Samantha","Sammy","Stephanie","Steven"],["Travis", "Tristain","Taylor","Tim","Tris"],["Ula","Ulysses","Unique","Umar","Ursule","Urijah","Uriel"],
    ["Victor","Vivian","Videl","Vaughn","Vincent","Veronica"],["Wayne","Walter","Warren","Whitney","Wheat"],["Xavier","Xzane","Xiong"],
    ["Yasmine","Yesenia","Yvette","Yvonne","Yuliana"],["Zeke","Zack","Zach","Zane","Zain","Zoey"]]
    newList = myList[y]
# Since x will be a single letter and that single letter represents a number, we can
# assign myList with a new variable that indexes the position of the x where a list of
# names are for your desired letter. x is now y
    z = randint(0,4)
# We will use z as the second index to random select an item within the list

    print(newList[z])

names()
