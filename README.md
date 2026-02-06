EvilTwin-Automator-V1 (Bản tối ưu cho iOS)
Công cụ tự động hóa thiết lập Lab bảo mật Wi-Fi (Evil Twin), được thiết kế riêng cho card mạng TP-Link TL-WN722N V1 và tối ưu hóa đường truyền cho các thiết bị di động (iPhone/Android).

Tổng quan
Dự án này giúp tự động hóa việc cấu hình các dịch vụ hostapd, dnsmasq và quy tắc iptables trên Kali Linux. 
Điểm khác biệt lớn nhất là bộ script này đã giải quyết triệt để vấn đề lag mạng và mất kết nối Internet thường gặp trên iPhone khi thực hiện tấn công MitM (Man-in-the-Middle).

Tính năng nổi bật
Khai hỏa một chạm: Chỉ với một lệnh Python, toàn bộ hệ thống NAT, IP Forwarding và các dịch vụ tấn công sẽ tự động khởi chạy.
Đặc trị lỗi Lag trên iPhone: Tích hợp kỹ thuật MTU Clamping để xử lý tình trạng kẹt tin nhắn Messenger và Facebook.
Vô hiệu hóa IPv6: Tự động chặn các yêu cầu IPv6 để ép thiết bị nạn nhân đi vào "luồng" IPv4 mà ta đã giăng lưới sẵn.
Tự động dọn dẹp: Khi nhấn Ctrl+C, Script sẽ tự động xóa sạch các quy tắc tường lửa và dừng dịch vụ, không làm ảnh hưởng đến việc sử dụng Internet bình thường của máy Kali sau đó.
Card mạng 1	TP-Link TL-WN722N V1 (Atheros AR9271)	Phát sóng Wifi giả (AP)
Card mạng 2	Intel Tiger Lake PCH CNVi	Bắt Wifi thật lấy Internet (WAN)
Hệ điều hành	Kali Linux	Máy tấn công
Hướng dẫn sử dụng
Tải mã nguồn về:
git clone https://github.com/leducbinh2/Wireshark-and-Wifi.git
cd Wireshark-and-Wifi
Chuẩn bị file cấu hình: Đảm bảo file hostapd.conf đã được chỉnh sang Channel 11 để tránh nhiễu sóng.
Chạy Tool:
sudo python3 attack.py
Lưu ý (Disclaimer)
Công cụ này chỉ được sử dụng cho mục đích nghiên cứu và học tập trong môi trường Lab an toàn. Tác giả (Sinh viên An ninh mạng) không chịu trách nhiệm cho bất kỳ hành vi sử dụng sai mục đích nào.
