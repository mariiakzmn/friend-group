"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


class Person:
    
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
        
        if relationship == "friend":
            person.relationships[self.name] = "friend"
            
        elif relationship == "parent":
            person.relationships[self.name] = "kid"
            
        
        pass
        
    
        
    

my_group = [Person("Jill", 26, "biologist", relationships={"Zalika":"friend"}),
            Person("Zalika", 28, "artist", relationships={"Jill":"friend"}),
            Person("John", 27, "writer"),
            Person("Nash", 34, "chef")     
]

my_group[0].set_relationship(my_group[1], "friend")