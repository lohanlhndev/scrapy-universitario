import cv2

imagem = cv2.imread('11_02.png')
cv2.imshow('teste', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()