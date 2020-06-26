import pypyodbc

def getConnection():
    conn = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-A32UCHC\SQLEXPRESS;'
    'Database=CRUDTest;'
    'Trusted_Connection=yes;'
)
    return conn