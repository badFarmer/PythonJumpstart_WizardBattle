class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name, self.level
        )


class Description:
    def __init__(self, adjective):
        self.adjective = adjective

    def __repr__(self):
        return '{}'.format(
            self.adjective
        )


class Location:
    def __init__(self, noun):
        self.noun = noun

    def __repr__(self):
        return '{}'.format(
            self.noun
        )


class ConcatText:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return '{}'.format(
            self.text
        )
