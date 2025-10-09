import student as Student
import database as Databse
import mysql.connector

def main():
    flag = True
    while(flag == True):
        try:
            db = Databse()
        except mysql.connector.Error as e:
            print("Lỗi kết nối", e)
        print("1.Thêm sinh viên\t2.Xóa Sinh viên\3.Tìm sinh viên theo ID\t4.Hiển thị danh sách\t5.Cập nhật sinh viên\t0.Thoát")
        a = input()
        if a=="1":
            id =    str(input("Nhập id sinh viên:"))
            ten = str(input("Nhập tên sinh viên:"))
            ngay = int(input("Nhập ngày sinh sinh viên:"))
            while(ngay < 1 and ngay > 31):
                print("Ngày sinh không hợp lệ, vui lòng nhập lại")
                ngay = int(input("Nhập ngày sinh sinh viên:"))
            thang = int(input("Nhập tháng sinh sinh viên:"))
            while(thang < 1 and thang > 12):
                print("Tháng sinh không hợp lệ, vui lòng nhập lại")
                thang = int(input("Nhập tháng sinh sinh viên:"))
            nam = int(input("Nhập năm sinh sinh viên:"))
            while(nam < 1800 and nam >2025):
                print("Năm sinh không hợp lệ, vui lòng nhập lại")
                nam = int(input("Nhập năm sinh sinh viên:"))
            lop = input("Nhập id sinh viên:")
            sv = Student(ten,id,ngay,thang,nam,lop)
            sv.themSinhVien(db)
        


