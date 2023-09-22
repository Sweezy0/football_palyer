with open("futbolcular.txt","r",encoding="UTF-8") as file:
    gs=list()
    bjk=list()
    fb=list()

    for satir in file:
        satir=satir[:-1]
        satir_elemanları=satir.split(",")
        
        if(satir_elemanları[1] == "Fenerbahçe"):
            fb.append(satir + "\n")
        elif(satir_elemanları[1] == "Galatasaray"):
            gs.append(satir + "\n")
        else:
            bjk.append(satir + "\n")

    with open("galatasaray.txt","w",encoding="UTF-8") as gs_file:
        for i in gs:
            gs_file.write(i)
        
    with open("fenerbahçe.txt","w",encoding="UTF-8") as fb_file:
        for i in fb:
            fb_file.write(i)

    with open("beşiktaş.txt","w",encoding="UTF-8") as bjk_file:
        for i in bjk:
            bjk_file.write(i)