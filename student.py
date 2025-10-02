class Student:
    def __init__(self,ten,id,ngay,thang,nam, lop):
        self.ten = ten
        self.id = id
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
        self.lop = lop
    
    @staticmethod
    def hienThiDanhSachSinhVien(db):
        query = "Select*from student"
        danh_sach = db.chay_lenh(query)
        danh_sach_tam = []
        if danh_sach:
            for val in danh_sach:
                ten,id,ngay,thang,nam,lop = val
                hoc_sinh = Student(ten,id,ngay,thang,nam,lop)
                danh_sach_tam.append(hoc_sinh)
            return danh_sach
        else:
            return []



    
