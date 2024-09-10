import pyodbc



list_time = ['7h-9h','9h-11h','13h-15h','15h-17h']

def checkhour(weekday):
    list = []
    # Kết nối đến cơ sở dữ liệu
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};Server=10.14.7.10;Database=NLP_Chatbot;UID=itdept;PWD=TH@c0123456;Encrypt=no")

    # Tạo đối tượng cursor để thực hiện thao tác trên cơ sở dữ liệu
    cursor = conn.cursor()
    for i in list_time:
        cursor.execute(f"SELECT {weekday} FROM SetMeetingRoom WHERE HOUR = ?", i)
        # Lấy tất cả giá trị của các dòng
        rows = cursor.fetchall()
        # Lấy giá trị của ô cần lấy trong mỗi dòng và append vào một list
        status = [row[0] for row in rows]
        if status[0] == 'empty':
            list.append(i)
    # Đóng kết nối
    conn.close()
    return list



