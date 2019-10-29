from luminus import sql_helper
from datetime import datetime


def get_students_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE status = 'enrolled' AND code = %(code)s ",
                                       {'code': code})


def get_students_for_TAs_by_coursecode(code):
    return  sql_helper.fetchall_to_dict("SELECT * FROM (Enrolls NATURAL JOIN Students) AS es WHERE es.code = %(code)s AND es.status ='COMPLETED' "
                                        "AND NOT EXISTS (SELECT 1 FROM Facilitate f WHERE f.code = %(code)s AND f.uname=es.uname)",
                                        {'code':code})


def add_student_for_TA_by_uname_coursecode_groupnum(uname,code,group_num):
    return sql_helper.fetchall_to_dict("INSERT INTO Facilitate VALUES (uname,coursecode,groupnum;"
                                       "INSERT INTO TAs VALUES (uname)"
                                       "WHERE NOT EXISTS (SELECT 1 FROM TAs t WHERE t.uname=uname);"
                                       "SELECT * FROM Facilitate f "
                                       "WHERE f.uname=%(uname)s and f.code=%(code)s and f.group_num=%(group_num)s)",
                                       {'code':code,'uname':uname,'group_num':group_num})


def add_student_to_tut_by_uname_coursecode_groupnum(uname, code, group_num):
    sql_helper.exec_sql('insert into Attend values (%(uname)s, %(code)s, %(group_num)s, %(date)s )',
                        {'uname': uname, 'code': code, 'group_num': group_num, 'date': datetime.now()})

    return sql_helper.fetchall_to_dict('SELECT * FROM Users NATURAL JOIN (Students NATURAL JOIN Attend) WHERE code = %(code)s AND group_num = %(group_num)s',
                                       {'code': code, 'group_num': group_num})


def get_student_enrolledbutnotattend_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM USERS u NATURAL JOIN Participators NATURAL JOIN (Students stu NATURAL JOIN Enroll e) "
                                       "WHERE e.code = %(code)s AND e.status ='enrolled' "
                                       "AND "
                                       "(NOT EXISTS (SELECT 1 FROM Attend a WHERE a.uname = stu.uname AND a.code = e.code ) )"
                                       ,{'code': code})


def get_students_by_coursecode_and_groupnum(code, group_num):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Attend)"
                                       " WHERE code = %(code)s AND group_num = %(group_num)s",
                                       {'code': code, 'group_num': group_num})


def get_requests_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users NATURAL JOIN participators NATURAL JOIN"
                                       " (Students NATURAL JOIN Enroll) WHERE status = 'requesting' AND code = %(code)s ",
                                       {'code': code})


def approve_requests(uname, code):
    return sql_helper.fetchall_to_dict("UPDATE Enroll SET status = 'enrolled'"
                                       "WHERE uname = %(uname)s AND code = %(code)s AND status='requesting'",
                                       {'uname': uname, 'code': code})


def reject_requests(uname, code):
    return sql_helper.fetchall_to_dict("UPDATE Enroll SET status = 'rejected'"
                                       "WHERE uname = %(uname)s AND code = %(code)s AND status='requesting'",
                                       {'uname': uname, 'code': code})


def get_ta_candidates_by_coursecode(code):
    return sql_helper.fetchall_to_dict("SELECT * FROM Users u NATURAL JOIN participators NATURAL JOIN (Students s NATURAL JOIN Enroll e) "
                                       "WHERE status = 'completed' AND code = %(code)s AND "
                                       "(NOT EXISTS(SELECT 1 FROM Assist a WHERE a.uname=s.uname AND a.code = e.code))",
                                       {'code': code})


def add_TA_by_uname_coursecode_group(uname, code):
    # for students that are yet not tutoring any course
    sql_helper.exec_sql('INSERT IGNORE INTO TAs VALUES(%(uname)s)', {'uname': uname})

    return sql_helper.exec_sql('INSERT IGNORE INTO Assist values(%(uname)s,  %(code)s)',
                               {'uname': uname,  'code': code})


def get_students_by_student_uname_and_coursecode(uname, code):
    return  sql_helper.fetchall_to_dict("SELECT * FROM (SELECT group_num FROM Attend NATURAL JOIN tutorials WHERE uname = %(uname)s and code = %(code)s) AS grp"
                                        " ,Attend AS atd, Users AS usr, Participators AS ptp WHERE grp.group_num = atd.group_num"
                                        " AND atd.code = %(code)s AND usr.uname=atd.uname AND ptp.uname=atd.uname",
                                        {'uname': uname, 'code': code})
