import sys
import pytest


class Student:
    def __init__(self, first_name, last_name, id, gpa_flibbit):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.gpa = gpa_flibbit  # Calls the setter with gpa_flibbit as the value.

    def get_first_name(self):
        return self.first_name

    @property
    def gpa(self):
        return self._gpa  # Using a private variable to store GPA, a float.

    @gpa.setter
    def gpa(self, value):
        if value < 0 or value > 4.0:
            raise ValueError("Invalid GPA value, must be between 0 and 4.0")
        else:
            self._gpa = value  # Assigning the value (a float) to the private variable.

    def is_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False


### Tests
# We're using pytest (https://docs.pytest.org/en/stable/) for testing.
# Installation methods:
#   uv pip install pytest
#   pip install pytest
#   brew install pytest


def test_sunnyday_student():
    """Test the sunny day scenario for the Student class."""

    student = Student("Sunny", "Day", 1, 3.8)
    assert student.get_first_name() == "Sunny"
    assert student.gpa == 3.8
    assert student.is_honor_roll() is True


def test_not_honor_roll_student():
    """Test a student who is not on the honor roll."""

    student = Student("Rainy", "Day", 2, 2.5)
    assert student.get_first_name() == "Rainy"
    assert student.gpa == 2.5
    assert student.is_honor_roll() is False


def test_first_name_property():
    """Test the first_name property of the Student class."""

    student = Student("First", "Name", 3, 3.0)
    assert student.get_first_name() == "First"


@pytest.mark.skip(reason="The full_name method is not implemented yet.")
def test_full_name_property():
    """Test the full name property of the Student class."""

    student = Student("Full", "Name", 4, 3.2)
    assert student.full_name() == "Full Name"


def test_invalid_gpa_constructor():
    """Test invalid GPA values during Student instantiation."""

    for invalid_gpa in [5.0, -1.0]:
        try:
            Student("Invalid", "GPA", 3, invalid_gpa)
            assert False, f"Expected ValueError for invalid GPA: {invalid_gpa}"
        except ValueError as e:
            pass


def test_invalid_gpa_assignment():
    """Test invalid GPA values when assigning to the gpa property."""

    student = Student("Assigned", "GPA", 4, 1)

    for invalid_gpa in [5.0, -1.0]:
        try:
            student.gpa = invalid_gpa
            assert False, "Expected ValueError for invalid GPA"
        except ValueError as e:
            pass


if __name__ == "__main__":
    sys.exit(pytest.main(sys.argv[1:] + ["-v", "--tb=short"]))

# EOF
