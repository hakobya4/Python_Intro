class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B

    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B


person_A_height = Height(2, 9)
person_B_height = Height(3, 9)
height_comp = person_A_height != person_B_height

print(height_comp)
