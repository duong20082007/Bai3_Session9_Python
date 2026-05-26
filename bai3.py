# Input:
# choice: Kiểu chuỗi nhập từ bàn phím.
# new_order: Kiểu chuỗi, có thể chứa khoảng trắng thừa hoặc ký tự viết thường.
# del_order: Kiểu chuỗi, có thể nhập không chuẩn form.

# Output:
# Màn hình Menu tương tác dạng văn bản (console text).
# Danh sách đơn hàng được in ra kèm số thứ tự (1, 2, 3...) theo vòng lặp chỉ số (index).
# Thông báo trạng thái thành công hoặc cảnh báo lỗi hợp lệ.

# Duy trì hệ thống: Sử dụng vòng lặp vô hạn while True và cấu trúc match...case để điều hướng menu mượt mà.
# Xử lý khoảng trắng và chữ hoa/thường: Mọi mã đơn hàng nhập vào đều phải đi qua bộ lọc .strip().upper() để chuẩn hóa về định dạng duy nhất 
# Hiển thị danh sách: Kiểm tra mảng rỗng bằng if not order_list. Nếu có dữ liệu, dùng vòng lặp truyền thống for i in range(len(order_list)) để in ra số thứ tự (i + 1) và giá trị (order_list[i]).
# Xóa đơn hàng an toàn: Tuyệt đối không dùng remove() ngay, mà phải dùng toán tử in để kiểm tra xem mã chuẩn hóa có tồn tại trong danh sách hay không. Nếu có mới xóa, tránh lỗi crash chương trình ValueError.
# Lọc lựa chọn ngoài danh mục: Dùng case _: làm chốt chặn cuối cùng. Bất kỳ thao tác nhập chữ cái hay số ngoài phạm vi 1-4 đều bị chặn lại và yêu cầu nhập lại.

order_list = ["GE001", "GE002", "GE003"]

while True:
    print("===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    match choice:
        case '1':
            if not order_list:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for i in range(len(order_list)):
                    print(f"{i + 1}. {order_list[i]}")
        case '2':
            new_order = input("Nhập mã đơn hàng mới: ")
            new_order_normalized = new_order.strip().upper()
            
            if new_order_normalized:
                order_list.append(new_order_normalized)
                print(f"Đã thêm thành công: {new_order_normalized}")
            else:
                print("Mã đơn hàng không được để trống!")
        case '3':
            del_order = input("Nhập mã đơn hàng cần xóa: ")
            del_order_normalized = del_order.strip().upper()
            
            if del_order_normalized in order_list:
                order_list.remove(del_order_normalized)
                print(f"Đã xóa thành công mã đơn hàng: {del_order_normalized}")
            else:
                print("Không tìm thấy mã đơn hàng cần xóa!")
        case '4':
            print("Thoát chương trình.")
            break 
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")