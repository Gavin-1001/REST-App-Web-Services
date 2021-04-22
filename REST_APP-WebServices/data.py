student_data = {}


def setup():
    from schema import Student

    global student_name_data, student_id_data, student_dob_data

    alice = Student(
        id="1",
        name="Alice",
        dob="1/1/2021",
    )
    bob = Student(
        id="2",
        name="Bob",
        dob="2/1/2021",
    )
    carl = Student(
        id="3",
        name="Carl",
        dob="3/1/2021",
    )
    d = Student(
        id="4",
        name="D",
        dob="04/01/2021",
    )
    eric = Student(
        id="5",
        name="Eric",
        dob="05/01/2021",
    )

    student_id_data = {
        "1" : alice,
        "2" : bon,
        "3" : carl,
        "4" : d,
        "5" : eric
        }
    student_name_data = {
        "Alice" : alice,
        "Bob" : bob,
        "Carl" : carl,
        "D" : d,
        "Eric" : eric
        }
    student_dob_data = {
        "01/01/2021" : alice,
        "02/01/2021" : bob,
        "03/01/2021" : carl,
        "04/01/2021" : d,
        "05/01/2021" : eric
        }

def get_name(name):
    return student_name_data.get(name)
def get_dob(dob):
    return student_dob_data.get(dob)
def get_id(id):
    return student_id_data.get(id)
