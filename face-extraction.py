import os
import cv2
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

# # exibe uma imagem de exemplo
# img1 = cv2.imread("dataset/images/maksssksksss0.png")
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# ex1 = ET.parse("dataset/annotations/maksssksksss0.xml").getroot()

# for object in ex1.findall("object"):
#   name = object.find("name").text
#   bndbox = object.find("bndbox")
#   xmin = int(bndbox.find("xmin").text)
#   ymin = int(bndbox.find("ymin").text)
#   xmax = int(bndbox.find("xmax").text)
#   ymax = int(bndbox.find("ymax").text)

#   label = "No Mask" if name == "without_mask" else "Mask"
#   color = (0, 255, 0) if label == "Mask" else (255, 0, 0)

#   faces1 = cv2.rectangle(img1, (xmin - 10 , ymin - 10), (xmax, ymax), color, 2)
#   cv2.putText(faces1, label, (xmin- 10, ymin - 13), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)

# plt.imshow(faces1)
# plt.show()

samples = []
labels = []
count_with_mask = 1
count_without_mask = 1

# percorre todo o dataset
for i in range(0, 853):
  root = ET.parse("dataset/annotations/maksssksksss" + str(i) + ".xml").getroot()
  # obtém os bounding boxes contidos no arquivo .xml
  for object in root.findall("object"):
    name = object.find("name").text
    bndbox = object.find("bndbox")
    xmin = int(bndbox.find("xmin").text)
    ymin = int(bndbox.find("ymin").text)
    xmax = int(bndbox.find("xmax").text)
    ymax = int(bndbox.find("ymax").text)

    img = cv2.imread("dataset/images/maksssksksss" + str(i) + ".png")
    img = img[ymin:ymax, xmin:xmax]
    # img = cv2.resize(img, (16, 16), interpolation=cv2.INTER_AREA)
    samples.append(img)

    # cria as pastas em que vão ser salvos as novas imagens
    if(os.path.exists("images/with_mask") == False):
      os.mkdir("images/with_mask")
    if(os.path.exists("images/without_mask") == False):
      os.mkdir("images/without_mask")

    if name == "with_mask" or name == "mask_weared_incorrect":
      filename = "images/with_mask/mask" + str(count_with_mask) + ".png"
      cv2.imwrite(filename, img)
      count_with_mask += 1
    elif name == "without_mask":
      filename = "images/without_mask/without_mask" + str(count_without_mask) + ".png"
      cv2.imwrite(filename, img)
      count_without_mask += 1
  
print("Com máscara:", count_with_mask) #3356
print("Sem máscara: ", count_without_mask) #718