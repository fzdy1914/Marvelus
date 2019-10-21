from luminus.managers import student_manager
from luminus.responses import success_json_response


def get_students_by_coursecode(request, code):
    students = student_manager.get_students_by_coursecode(code)
    return success_json_response({'students': students})


def get_students_by_coursecode_and_groupnum(request, code, group):
    students = student_manager.get_students_by_coursecode_and_groupnum(code, group)
    return success_json_response({'students': students})