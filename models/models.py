


class Klub:
    def __init__(self, name, description, stadium, location, foundation):
        self.name = name
        self.description = description
        self.stadium = stadium
        self.location = location
        self.foundation = foundation


    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "stadium": self.stadium,
            "location": self.location,
            "foundation": self.foundation
        }
    
    def from_dict(data):
        return Klub(
            data["name"],
            data["description"],   
            data["stadium"],
            data["location"],
            data["foundation"]
            )
    
    def __str__(self):
        return (f"Naziv: {self.name}\n"
                f"Opis: {self.description}\n"
                f"Stadion: {self.stadium}\n"
                f"Lokacija: {self.location}\n"
                f"Godina osnutka: {self.foundation}")
        
            


        


