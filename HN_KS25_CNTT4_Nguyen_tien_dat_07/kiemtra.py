transaction_list = [{
    "id" : "TX001",
    "coment" : "Thu tien ban hang thang 5",
    "loai_giao_dich" : "Thu",
    "price" : 25000000,
    "amount" : 10,
    "tien_thuc_te" :27500000,
    "quy_mo" : "Lớn"
}]
# phân loại hạng mục quy mô 
def classify_scale(tien):
    if tien >= 50000000:
        return "Rất lớn"
    elif tien >= 10000000:
        return "Lớn"
    elif tien >= 2000000:
        return "Vừa"
    else:
        return "Nhỏ"


# kiểm tra trùng ID
def check_duplicate_id(transaction_list, transaction_id):
    for transaction in transaction_list:
        if transaction["id"] == transaction_id:
            return True
    return False


# tính tiền thực tế
def calculate_actual_money(phat_sinh, thue_suat):
    return phat_sinh * (1 + thue_suat / 100)
# hiển thị danh sách

def display_transaction(transaction):
    if len(transaction) == 0:
        print("Danh sách hiện đang rỗng !")
    else :
        print(f"{'STT' :<6} | {'Mã TX' :<8} | {'Nội dung' :<20} | {'Loại (Thu/Chi)' :<10} | {'Số tiền gốc' :<10} | {'Thuế suất' :<10} |{'Số tiền thực tế' :<10} |{'Phân loại quy mô' :<15} ")
        print("-" * 100)
        for stt,value in enumerate(transaction,start=1):
            id = value["id"]
            noi_dung = value["coment"]
            giao_dich = value["loai_giao_dich"]
            tien_goc = value["price"]
            thue_suat = value["amount"]
            tien_thuc_te = value["tien_thuc_te"]
            quy_mo = value["quy_mo"]
            print(f"{stt : <6} | {id :<8} | {noi_dung :<20} | {giao_dich :<10} | {tien_goc :<10} | {thue_suat :<10} |{tien_thuc_te :<10} |{quy_mo :<15} " )
        print("-" *100)

# thêm giao dịch
def add_transaction(transaction):
    while True:
        transaction_id = input("Nhập mã giao dịch mới: ").strip().upper()
        if transaction_id == "":
            print("Mã giao dịch không được rỗng!")
            continue
        if check_duplicate_id(transaction,transaction_id):
            print("Mã giao dịch đã tồn tại!")
            continue
        break
    while True:
        coment = input("Nhập nội dung giao dịch: ").strip()
        if coment == "":
            print("Nội dung không được rỗng!")
            continue
        break

    while True:
        loai = input("Nhập loại (Thu/Chi): ").strip().title()
        if loai not in ["Thu", "Chi"]:
            print("Chỉ được nhập Thu hoặc Chi!")
            continue
        break
    while True:
        try:
            price_new = float(input("Nhập số tiền phát sinh: "))
            if price_new <= 0:
                print("Số tiền phải lớn hơn 0!")
                continue
            break
        except:
            print("Vui lòng nhập số!")
    while True:
        try:
            amount_new = float(input("Nhập thuế suất: "))
            if amount_new < 0:
                print("Thuế suất phải >= 0!")
                continue
            break
        except:
            print("Vui lòng nhập số!")

    thuc_te = calculate_actual_money( price_new,amount_new)
    quy_mo = classify_scale(thuc_te)
    new_transaction = {
        "id": transaction_id,
        "coment": coment,
        "loai_giao_dich": loai,
        "price": price_new,
        "amount": amount_new,
        "tien_thuc_te": thuc_te,
        "quy_mo": quy_mo
    }
    transaction.append(new_transaction)
    print("Thêm giao dịch thành công!")


# cập nhật giao dịch
def update_transaction(transaction):
    transaction_id = input("Nhập mã giao dịch cần cập nhật: ").strip().upper()
    found = None
    for item in transaction:
        if item["id"] == transaction_id:
            found = item
            break
    if found is None:
        print("Không tìm thấy mã giao dịch!")
        return
    coment_new = input("Nhập nội dung mới: ").strip()
    while True:
        loai_new = input("Nhập loại mới (Thu/Chi): ").strip().title()
        if loai_new not in ["Thu", "Chi"]:
            print("Chỉ được nhập Thu hoặc Chi!")
            continue
        break
    while True:
        try:
            price_new = float(input("Nhập số tiền mới: "))
            if price_new <= 0:
                print("Số tiền phải lớn hơn 0!")
                continue
            break
        except:
            print("Vui lòng nhập số!")

    while True:
        try:
            amount_new = float(input("Nhập thuế suất mới: "))
            if amount_new < 0:
                print("Thuế suất phải >= 0!")
                continue
            break
        except:
            print("Vui lòng nhập số!")

    thuc_te = calculate_actual_money(price_new,amount_new)
    quy_mo = classify_scale(thuc_te)
    found["coment"] = coment_new
    found["loai_giao_dich"] = loai_new
    found["price"] = price_new
    found["amount"] = amount_new
    found["tien_thuc_te"] = thuc_te
    found["quy_mo"] = quy_mo

    print("Cập nhật thành công!")


# xóa giao dịch
def remove_transaction(transaction):
    transaction_id = input("Nhập mã giao dịch cần xóa: ").strip().upper()
    for item in transaction:
        if item["id"] == transaction_id:
            confirm = input("Bạn có chắc muốn xóa giao dịch này không? (Y/N): ").strip().upper()
            if confirm == "Y":
                transaction.remove(item)
                print("Xóa thành công!")
            else:
                print("Đã hủy xóa!")
            return

    print("Không tìm thấy giao dịch!")


# tìm kiếm giao dịch
def search_transaction(transaction):
    key = input("Nhập mã hoặc nội dung cần tìm: ").strip().lower()
    result = []
    for item in transaction:
        if (
            key == item["id"].lower()
            or key in item["coment"].lower()
        ):
            result.append(item)
    if len(result) == 0:
        print("Không tìm thấy giao dịch!")
    else:
        display_transaction(result)


# thống kê giao dịch
def statistics_transaction(transaction):

    rat_lon = 0
    lon = 0
    vua = 0
    nho = 0

    for item in transaction:
        if item["quy_mo"] == "Rất lớn":
            rat_lon += 1
        elif item["quy_mo"] == "Lớn":
            lon += 1
        elif item["quy_mo"] == "Vừa":
            vua += 1
        else:
            nho += 1

    print("\n----- THỐNG KÊ DÒNG TIỀN -----")
    print(f"Rất lớn : {rat_lon}")
    print(f"Lớn     : {lon}")
    print(f"Vừa     : {vua}")
    print(f"Nhỏ     : {nho}")


# phân loại lại toàn bộ
def recalculate_scale(transaction):
    for item in transaction:
        item["quy_mo"] = classify_scale(item["tien_thuc_te"])
    print("Đã cập nhật lại toàn bộ quy mô!")
def main():
    while True:
        print(""" --- Quản lý khoản dao dịch ---


1.Hiển thị nhật ký giao dịch
2.Ghi nhận giao dịch mới
3.Cập nhật chứng từ giao dịch
4.Xóa giao dịch lỗi
5.Tìm kiếm giao dịch
6.Thống kê tổng dòng tiền
7.Phân loại quy mô tự động    
8.Thoát chương trình""")
        choice = input("Nhập lựa chọn của bạn(1-8): ")
        match choice:
            case "1":
                display_transaction(transaction_list)
            case "2":
                add_transaction(transaction_list)
            case "3" :
                update_transaction(transaction_list)
            case "4":
                remove_transaction(transaction_list)
            case "5":
                search_transaction(transaction_list)
            case "6":
                statistics_transaction(transaction_list)
            case "7":
                recalculate_scale(transaction_list)
            case "8" :
                print("Thoát chương trình !")
                break
            case _ :
                print("Vui lòng nhập đúng định dạng hoặc số từ 1-8 !")
                continue
main()