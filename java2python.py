class Student:
    def __init__(self, first_name, last_name, id, gpa_flibbit):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.gpa = gpa_flibbit # Calls the setter with gpa_flibbit as the value.

    def get_first_name(self):
        return self.first_name

    @property
    def gpa(self):
        return self._gpa # Using a private variable to store GPA, a float.

    @gpa.setter
    def gpa(self, value):
        if value < 0 or value > 4.0:
            raise ValueError('Invalid GPA value, must be between 0 and 4.0')
        else:
            self._gpa = value # Assigning the value (a float) to the private variable.

    def is_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False

if __name__ == '__main__':
    print("Student Class Example!!")
    pupil1 = Student('Chicken', 'Little', 1, 3.5)
    pupil2 = Student('Big Bad', 'Wolf', 2, 2.3)
    pupil3 = Student('Charcoal', 'Sheep', 3, 3.3)
    print(pupil1.get_first_name())
    print(pupil2.get_first_name())
    print(pupil3.gpa)
    print(pupil1.is_honor_roll())
    print(pupil2.is_honor_roll())
    print(pupil3.is_honor_roll())
    print(pupil2.gpa)

    print("** Testing invalid GPA value being assigned:")
    try:
        pupil1.gpa = 5
        print(f"\tFailed to return an error: {pupil1.gpa}")
    except ValueError as e:
        print(f"\tSuccessfully returned an error: {e}")

    print("** Testing invalid GPA value being passed to constructor:")
    try:
        Student("Bad Student", "Example", 4, -1.3)
        print(f"\tFailed to return an error")
    except ValueError as e:
        print(f"\tSuccessfully returned an error: {e}")