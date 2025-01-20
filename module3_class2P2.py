
#Error handling

try:
    with open("abc.text","r") as file:
     content=file.read()
     num=10/0
except Exception as e:
      print("....")

finally:
    print("something went wrong") #gental exit     