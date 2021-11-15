import cv2
import numpy as np
#Autores: Norbey Marin Moreno, Julián Mauricio Flórez

def tomarPunto(idImg, image_draw, colorPunto):
    points = []
    def click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append([x, y])
    cv2.namedWindow(idImg)
    cv2.setMouseCallback(idImg, click)
    points1 = []
    point_counter = 0
    while True:
        cv2.imshow(idImg, image_draw)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):
            points1 = points.copy()
            points = []
            break
        if len(points) > point_counter:
            point_counter = len(points)
            cv2.circle(image_draw, (points[-1][0], points[-1][1]), 3, colorPunto, -1)
            print(points)
    cv2.destroyWindow(idImg) #una vez selecionados los puntos cierra la imagen
    return points1 # retorna los puntos



red = [0, 0, 255] #color para pintar puntos

cap = cv2.VideoCapture("E:\Documentos\Maestria AI\Segundo Semestre\Geometria Computacional\Proyecto/F1 2021 Brazil Interlagos Alonso low.mp4")
obj_detec = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=40, detectShadows=False)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

ret, frame = cap.read()
punto1 = tomarPunto("Primer frame", frame, red) #llama al metodo que pinta rojo
punto = np.array(punto1) #pasa los fumtos a un array para el metodo cv2.drawContours

while True:
    ret, frame = cap.read()
    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    alto, ancho, _ = frame.shape
    cv2.drawContours(frame, [punto], -1, (0, 0, 255), 2)# dibuja los puntos capturados con click
    imgMask = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)#imagen para usar de mascara
    imgMask = cv2.drawContours(imgMask, [punto], -1, 255, -1)# dibuja en blanco el area del polygono que encierra los puntos
    imgMaskArea = cv2.bitwise_and(frame, frame, mask=imgMask)# muestra sobre la imagen principal solo lo que esta en la mascara

    mask = obj_detec.apply(imgMaskArea) #aplica el sustractor de fondo sobre la imagen mascara


    contornos, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#encuentra los contornos
    for cont in contornos:
        area = cv2.contourArea(cont)#calcula el area de cada contorno
        if area > 500: #visualiza los contornos con areas mayores

            x, y, w, h = cv2.boundingRect(cont)# extrae los puntos del rectangulo de cada contorno
            #calcula el punto medio de cada rectangulo
            centroX = int((2 * x + w) // 2)
            centroY = int((2 * y + h) // 2)
            cv2.circle(frame, (centroX, centroY), 5, red, -1)#dibuja un circulo
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)# dibuja rectangulos sobre cada contorno


    cv2.imshow("area de zeros", imgMask)
    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)

    key = cv2.waitKey(30)
    if key ==27:
        break
cap.release()
cv2.destroyAllWindows()
