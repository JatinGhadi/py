class person:
    hands=1
    legs=2
    
    def walking(self):
        print("Hi.. I'm Human. I can walk")

    def talking(self):
        print("Hi.. I'm Human. I can walk")

human1=person()
print(human1.hands)
print(human1.legs)
human1.walking()
human1.talking()
print(type(human1))
