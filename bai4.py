# Input:
# choice / sub_choice: kiểu str
# order_code, order_status: kiểu str
# position: nhập vào là str, cần chuyển sang int

# Output:
# Hiển thị danh sách đánh số thứ tự từ 1.
# Bảng thống kê số lượng đơn hàng theo từng trạng thái.
# Các thông báo thành công hoặc cảnh báo lỗi

# Giải pháp: 
# Cấu trúc điều hướng: Sử dụng 2 vòng lặp while True. Một vòng cho Menu chính, một vòng lồng bên trong cho Menu cập nhật. 
# Dùng match...case để bắt lựa chọn.
# Xử lý chuỗi: Khi nhận đầu vào mã và trạng thái, sử dụng nối chuỗi: .strip().upper() để đảm bảo dữ liệu luôn sạch và 
# đồng nhất trước khi ghép lại bằng f-string f"{code} - {status}".
# Khởi tạo 4 biến đếm bằng 0 từ đầu. 
# Dùng vòng lặp for quét qua danh sách, dùng hàm .split(" - ") để tách chuỗi thành mảng 2 phần tử, 
# lấy phần tử thứ 2 để so sánh và tăng biến đếm

order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    match choice:
        case '1':
            if not order_list:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for i, order in enumerate(order_list, start=1):
                    print(f"{i}. {order}")

        case '2':
            while True:
                print("----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("1. Thêm đơn hàng mới")
                print("2. Sửa đơn hàng theo vị trí")
                print("3. Xóa đơn hàng theo vị trí")
                print("4. Quay lại menu chính")
                
                sub_choice = input("Nhập lựa chọn (1-4): ").strip()
                
                match sub_choice:
                    case '1':
                        code = input("Nhập mã đơn hàng: ").strip().upper()
                        status = input("Nhập trạng thái: ").strip().upper()
                        if code and status:
                            new_order = f"{code} - {status}"
                            order_list.append(new_order)
                            print(f"Đã thêm: {new_order}")
                        else:
                            print("Mã hoặc trạng thái không được để trống!")
                    case '2':
                        pos_input = input("Nhập vị trí đơn hàng cần sửa: ").strip()
                        if pos_input.isdigit():
                            pos = int(pos_input)
                            if 1 <= pos <= len(order_list):
                                new_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                                new_status = input("Nhập trạng thái mới: ").strip().upper()
                                if new_code and new_status:
                                    updated_order = f"{new_code} - {new_status}"
                                    order_list[pos - 1] = updated_order
                                    print("Cập nhật thành công!")
                                else:
                                    print("Dữ liệu không được để trống!")
                            else:
                                print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            print("Vị trí không hợp lệ! Vui lòng nhập số.")
                    case '3':
                        pos_input = input("Nhập vị trí đơn hàng cần xóa: ").strip()
                        if pos_input.isdigit():
                            pos = int(pos_input)
                            if 1 <= pos <= len(order_list):
                                deleted_order = order_list.pop(pos - 1)
                                print(f"Đã xóa đơn hàng: {deleted_order}")
                            else:
                                print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            print("Vị trí không hợp lệ! Vui lòng nhập số.")
                    case '4':
                        print("Quay lại menu chính...")
                        break
                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        case '3':
            pending_count = 0
            delivering_count = 0
            completed_count = 0
            cancelled_count = 0
            
            for order in order_list:
                parts = order.split(" - ")
                if len(parts) == 2:
                    status = parts[1] 
                    if status == "PENDING":
                        pending_count += 1
                    elif status == "DELIVERING":
                        delivering_count += 1
                    elif status == "COMPLETED":
                        completed_count += 1
                    elif status == "CANCELLED":
                        cancelled_count += 1
                        
            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print(f"PENDING: {pending_count}")
            print(f"DELIVERING: {delivering_count}")
            print(f"COMPLETED: {completed_count}")
            print(f"CANCELLED: {cancelled_count}")
            print(f"Tổng số đơn hàng: {len(order_list)}")
        case '4':
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")