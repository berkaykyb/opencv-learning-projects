import cv2
import pytesseract
from PIL import Image

image_path = ("./02-text_detection/tabela.jpg")

# Görüntüyü oku
image = cv2.imread(image_path)

# OCR için PIL formatına çevir
pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# Tesseract'tan kelime + koordinat bilgisi al
data = pytesseract.image_to_data(pil_image, lang="eng", output_type=pytesseract.Output.DICT)

n_boxes = len(data["text"])

for i in range(n_boxes):
    text = data["text"][i].strip()

    if text != "":
        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]

        # Yeşil kutu
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Kutunun ALTINA yazıyı yaz
        cv2.putText(image, text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow("OCR with Bounding Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
