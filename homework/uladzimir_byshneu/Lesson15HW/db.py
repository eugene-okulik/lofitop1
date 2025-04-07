import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES ('MIXI', 'ORACLE')")
student_id = cursor.lastrowid
add_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
add_books,(
        ('PELEVIN', student_id),
        ('PELEVIN2', student_id),
        ('PELEVIN3', student_id)
          )
)
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) "
    "VALUES ('TOP GRUPPA', 'feb 2025', 'apr 2025')"
)
group_student_id = cursor.lastrowid
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_student_id, student_id))
cursor.execute("INSERT INTO subjets (title) VALUES ('История экономики')")
subject1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES ('Геология')")
subject2_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Геология Беларуси', %s)", (subject1_id,))
lesson1_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Геология Европы', %s)", (subject2_id,))
lesson2_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('История экономики: древний мир', %s)", (subject1_id,))
lesson3_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('История экономики: средневековье', %s)",
               (subject2_id,))
lesson4_id = cursor.lastrowid

add_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    add_marks, [
        (10, lesson1_id, student_id),
        (10, lesson2_id, student_id),
        (9, lesson3_id, student_id),
        (8, lesson4_id, student_id),
    ]
)
db.commit()
cursor.execute("SELECT value FROM marks WHERE student_id = %s", (student_id,))
print(cursor.fetchall())
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())
all_info = '''
SELECT *
FROM students st
LEFT JOIN `groups` g ON st.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = st.id
LEFT JOIN marks m ON m.student_id = st.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets s ON l.subject_id = s.id
where st.id = %s
'''
cursor.execute(all_info, (student_id,))
print(cursor.fetchall())
db.close()
