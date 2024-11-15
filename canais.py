def readImage(filepath):
    with open(filepath, "r") as image:
        image.readline().strip()
        
        line = image.readline().strip()
        
        width, height = map(int, line.split())
        grayscaleBits = int(image.readline().strip())
        
        conteudo = image.read()
        numeros = conteudo.split()
        pixels = []
        row = []
        rgb = []
        for num in numeros:
            rgb.append(int(num))
            
            if len(rgb) == 3:
                row.append(rgb)
                rgb = []
            
            if len(row) == width: 
                pixels.append(row)
                row = []
        
    return pixels, grayscaleBits, width, height

def separarCor(pixels, manterCor, valor, width, height):
    convertedPixels = []
    for y in range(height):
        fixedRow = []
        for x in range(width):
            redValue = int(pixels[y][x][0])
            greenValue = int(pixels[y][x][1])
            blueValue = int(pixels[y][x][2])
            
            if manterCor == 0:
                greenValue = blueValue = valor
            elif manterCor == 1:
                redValue = blueValue = valor
            else:
                redValue = greenValue = valor
                
            rgb = [redValue, greenValue, blueValue]
            fixedRow.append(' '.join(map(str, rgb)))
        convertedPixels.append(fixedRow) 
            
    return convertedPixels


def saveIMG(filename, type, bits, pixels, width, height):
    with open(filename, "w") as newImage:
        newImage.write(type + "\n")
        newImage.write(str(width) + " " + str(height) + "\n")
        newImage.write(str(bits) + "\n")
        
        for row in pixels:
            newImage.write(" ".join(map(str, row)) + "\n")
        print("saved")
            
originalIMG = "Fig4.ppm"

pixels, bits, width, height = readImage(originalIMG)
limiar = 40
convertedColor = separarCor(pixels, 2, 255, width, height)

output = "media.pgm"

saveIMG("azul reduzido.ppm", "P3", bits, convertedColor, width, height)