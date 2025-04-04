# Sử dụng image Odoo 16.0 làm base image
FROM odoo:16.0

# Cập nhật và cài đặt thư viện googletrans
RUN pip3 install googletrans==4.0.0-rc1
RUN pip3 install gtts
