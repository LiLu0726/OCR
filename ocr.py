import cv2
import requests
import io

img = cv2.imread("test.jpg")
height , width , channel = img.shape

# Cutting image
roi = img [0: height, 0 : width]

#ocr
url_api = "https://api.ocr.space/parse/image"
channel,compressedimage = cv2.imencode(".jpg" , roi , [1,90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,files = {"test.jpg":file_bytes},
              data = {"apikey":"helloworld"})

print(result.content.decode())

cv2.imshow("Roi",roi)
cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows();