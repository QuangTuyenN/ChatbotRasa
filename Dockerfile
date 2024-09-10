FROM python:3.8
WORKDIR /app
COPY . .
# Sao chép tệp start.sh vào container
COPY start.sh /start.sh
# Đặt quyền thực thi cho tệp start.sh
RUN chmod +x /start.sh
RUN pip install rasa
RUN pip install bs4

EXPOSE 5005
EXPOSE 5055
EXPOSE 8080
# CMD để thực thi lệnh trong tệp start.sh
CMD ["/start.sh"]







