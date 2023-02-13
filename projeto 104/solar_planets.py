import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("mostrar imagem",img)

cv2.putText(img,
             "Sol",
             (0,200),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (255,0,0)               
             )

cv2.putText(img,
             "Mercurio",
             (100,200),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,  
             (0,0,255)               
             )

cv2.putText(img,
             "Venus",
             (170,230),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,  
             (0,255,0)               
             )

cv2.putText(img,
             "Terra",
             (270,200),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,  
             (0,0,255)               
             )

cv2.putText(img,
             "Marte",
             (370,230),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,  
             (255,0,0)               
             )

cv2.putText(img,
             "jupter",
             (430,200),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,255,0)               
             )

cv2.putText(img,
             "Saturno",
             (670,200),
             cv2.FONT_HERSHEY_COMPLEX,
             1.3,  
             (255,0,0)               
             )

cv2.putText(img,
             "Urano",
             (960,200),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,  
             (0,0,255)               
             )

cv2.putText(img,
             "Netuno",
             (1110,200),
             cv2.FONT_HERSHEY_COMPLEX,
             0.7,  
             (0,255,0)               
             )

cv2.imshow("Resultado",img) 
cv2.waitKey(0) 
cv2.imwrite("Solar_systemwithname.jpg",img)