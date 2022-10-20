"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


class Person:
    
    
    reciprocal_relationships = ["friend",
                                "colleage",
                                "sibling",
                                "partner",
                                "cousin"]
    
    other_relationships = {"parent":"kid",
                           "kid":"parent",
                           "tennant":"landlord",
                           "landlord":"tennant"}
    
    def __init__(self, name, age, job=None, relationships=None):
        self.name = name
        self.age = age
        self.job = job
        
        if relationships:
            self.relationships =  relationships
        else:
            self.relationships = {}

    
    def set_relationship(self, person, relationship):
        
        self.relationships[person.name] = relationship
        
        
        if relationship in self.reciprocal_relationships:
            person.relationships[self.name] = relationship
        elif relationship in self.other_relationships.keys():
            person.relationships[self.name] = self.other_relationships[relationship]
                
    
        
    

my_group = {"Jill"  : Person("Jill",   26, "biologist"),
            "Zalika": Person("Zalika", 28, "artist"),
            "John"  : Person("John",   27, "writer"),
            "Nash"  : Person("Nash",   34, "chef")     
}

# Set relationship of Jill<->Zalika as "friend"
my_group["Jill"].set_relationship(my_group["Zalika"], "friend")
my_group["Jill"].set_relationship(my_group["John"], "partner") 


for p in my_group.keys():
    print(f"{p}'s Relationships are: ")
    print(my_group[p].relationships)


