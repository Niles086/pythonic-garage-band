class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        raise NotImplementedError("Subclasses must implement play_solo method")

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, instrument="guitar")

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, instrument="bass")

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, instrument="drums")

    def play_solo(self):
        return "rattle boom crash"


class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

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
        return cls.instances


# Example usage:
if __name__ == "__main__":
    guitarist1 = Guitarist("Kurt Cobain")
    bassist1 = Bassist("Krist Novoselic")
    drummer1 = Drummer("Dave Grohl")

    band1 = Band("Nirvana", [guitarist1, bassist1, drummer1])

    print(band1.play_solos())
    print(Band.to_list())
