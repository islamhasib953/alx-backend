import requests

# رابط الملف على الإنترنت
url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240831T192226Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=24f7b97df6183a9b063664bcab855a9910e40eb60f76571588b8219ff1b42bfb"

# تحميل الملف
response = requests.get(url)

# حفظ الملف محليًا
with open("Popular_Baby_Names.csv", "wb") as file:
    file.write(response.content)
