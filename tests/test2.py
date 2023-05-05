#bolja čitljivost slike
import cv2 as cv

img = cv.imread('ploca1.jpg')

#scale: veličina skalirane slike u odnosu na početnu
scale = 0.3
new_width = int(img.shape[1]*scale)
new_height = int(img.shape[0]*scale)

img = cv.resize(img, (new_width, new_height))
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

#source = img, sve svijetlije od 22 ide u bijelu, tamnije ide u crnu
#255 je boja "bijele" u koju će se posvijetliti, 
#THRESH_BINARY je tip algoritma koji se koristi
_, result = cv.threshold(img, 100, 255, cv.THRESH_BINARY)

#adaptive threshold ne postavlja sve na istu vrijednost kao kod iznad,
#nego bira koje će pixele posvijetliti više, a koje manje, threshold nije fiksan
#ogromna pomoć pri slici s nejednakim osvjetljenjem
#source, max value boje sive, algoritam za adaptive, binary algoritam kao i gore
#sa zadnje dvije vrijednosti se moramo igrati: prvi je broj susjednih pixela koje gledamo
#drugi je neka konstanta idk
adaptive1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 
                                391, 0)


#igra
adaptive2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 
                                391, 0)

cv.imshow('Image', img)
#cv.imshow('Result', result)
cv.imshow('Adaptive1', adaptive1)
#cv.imshow('Adaptive2', adaptive2)

#bez ovoga, slika bi se pokazala i odmah nestala
#zato stavljamo value 0
cv.waitKey(0)
cv.destroyAllWindows()