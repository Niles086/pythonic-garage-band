class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        raise NotImplementedError("Subclasses must implement play_solo method")

    def __str__(self):
        return f"{self.name} - {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.instrument}')"


class Guitarist(Musician):
    def play_solo(self):
        return f"{self.name} is playing a guitar solo"


class Bassist(Musician):
    def play_solo(self):
        return f"{self.name} is playing a bass solo"


class Drummer(Musician):
    def play_solo(self):
        return f"{self.name} is playing a drum solo"


class Band:
    bands_list = []

    def __init__(self, name):
        self.name = name
        self.members = []
        Band.bands_list.append(self)

    def add_musician(self, musician):
        if isinstance(musician, Musician):
            self.members.append(musician)

    def play_solos(self):
        solos = [member.play_solo() for member in self.members]
        return solos

    def __str__(self):
        return f"{self.name} - Members: {', '.join(str(member) for member in self.members)}"

    def __repr__(self):
        return f"Band('{self.name}')"

    @classmethod
    def to_list(cls):
        return cls.bands_list


# Example usage:
if __name__ == "__main__":
    guitarist1 = Guitarist("John", "Electric Guitar")
    bassist1 = Bassist("Paul", "Bass Guitar")
    drummer1 = Drummer("Ringo", "Drums")

    band1 = Band("The Beatles")
    band1.add_musician(guitarist1)
    band1.add_musician(bassist1)
    band1.add_musician(drummer1)

    print(band1.play_solos())

    print(Band.to_list())
