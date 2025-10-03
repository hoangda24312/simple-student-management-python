class Student:
    def __init__(self,ten,id,ngay,thang,nam, lop):
        self.ten = ten
        self.id = id
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
        self.lop = lop
    
    def themSinhVien(self,db):
        query = "Insert into student (id,ten,ngay,thang,nam,lop) values (%s,%s,%s,%s,%s,%s)"
        params = (self.id,self.ten,self.ngay,self.thang,self.nam,self.lop)
        db.chay_lenh(query,params)
    
    def xoaSinhVien(self,db):
        query = "Delete*from student where id=%s"
        db.chay_lenh(query,(self.id,))

    

    @staticmethod
    def timSinhVien(db, id):
        query = "Select*from student where id=%s"
        danh_sach = db.select(query,(id,))
        danh_sach_tam = []
        if danh_sach:
            for val in danh_sach:
                id,ten,ngay,thang,nam,lop = val
                hoc_sinh = Student(id,ten,ngay,thang,nam,lop)
                danh_sach_tam.append(hoc_sinh)
            return danh_sach_tam
        else:
            return []

    
    @staticmethod
    def hienThiDanhSachSinhVien(db):
        query = "Select*from student"
        danh_sach = db.select(query)
        danh_sach_tam = []
        if danh_sach:
            for val in danh_sach:
                id,ten,ngay,thang,nam,lop = val
                hoc_sinh = Student(ten,id,ngay,thang,nam,lop)
                danh_sach_tam.append(hoc_sinh)
            return danh_sach
        else:
            return []



    
