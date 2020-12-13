from tkinter import *
import random
import pygame

pygame.mixer.init()

root = Tk()
root.tk_setPalette("light blue")
root.attributes("-fullscreen", 1)

def okunus():
    o1 = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on", "on bir", "on iki",
          "on üç", "on dört", "on beş", "on altı", "on yedi", "on sekiz", "on dokuz", "yirmi"]

    birlik_1 = {"sıfır": 0,
                "bir": 1,
                "iki": 2,
                "üç": 3,
                "dört": 4,
                "beş": 5,
                "altı": 6,
                "yedi": 7,
                "sekiz": 8,
                "dokuz": 9,
                "on": 10,
                "on bir": 11,
                "on iki": 12,
                "on üç": 13,
                "on dört": 14,
                "on beş": 15,
                "on altı": 16,
                "on yedi": 17,
                "on sekiz": 18,
                "on dokuz": 19}

    o2 = []
    o3 = []
    o4 = []
    o7 = []
    o10 = []
    o13 = []
    o16 = []
    
    o5 = [["", ""], ["", ""], ["", ""], ["", ""]]
    o6 = [["", ""], ["", ""], ["", ""], ["", ""]]
    o8 = [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]
    o9 = [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]
    
    o11 = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
    o12 = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]

    o14 = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]
    o15 = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]

    o17 = [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]
    o18 = [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]

    on_1 = ["yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    on_2 = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]

    yuz = ["yüz", "iki yüz", "üç yüz", "dört yüz", "beş yüz", "altı yüz", "yedi yüz", "sekiz yüz", "dokuz yüz"]
    on_3 = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    bin_1 = ["bin", "bir bin" ,"iki bin", "üç bin", "dört bin", "beş bin", "altı bin", "yedi bin", "sekiz bin", "dokuz bin"]
    yuz_1 = ["", "yüz", "iki yüz", "üç yüz", "dört yüz", "beş yüz", "altı yüz", "yedi yüz", "sekiz yüz", "dokuz yüz"]

    on_bin = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    on_bin_1 = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    yuzluk = {"yüz": 1,
              "iki yüz": 2,
              "üç yüz": 3,
              "dört yüz": 4,
              "beş yüz": 5,
              "altı yüz": 6,
              "yedi yüz": 7,
              "sekiz yüz": 8,
              "dokuz yüz": 9}

    yuzluk_1 = {"": 0,
                "yüz": 1,
                "iki yüz": 2,
                "üç yüz": 3,
                "dört yüz": 4,
                "beş yüz": 5,
                "altı yüz": 6,
                "yedi yüz": 7,
                "sekiz yüz": 8,
                "dokuz yüz": 9}

    binlik = {"bin": 1,
              "iki bin": 2,
              "üç bin": 3,
              "dört bin": 4,
              "beş bin": 5,
              "altı bin": 6,
              "yedi bin": 7,
              "sekiz bin": 8,
              "dokuz bin": 9}

    binlik_1 = {"bin": 0,
                "bir bin": 1,
                "iki bin": 2,
                "üç bin": 3,
                "dört bin": 4,
                "beş bin": 5,
                "altı bin": 6,
                "yedi bin": 7,
                "sekiz bin": 8,
                "dokuz bin": 9}

    onluk_1 = {"": 0,
             "on": 1,
             "yirmi": 2,
             "otuz": 3,
             "kırk": 4,
             "elli": 5,
             "altmış": 6,
             "yetmiş": 7,
             "seksen": 8,
             "doksan": 9}

    onluk_2 = {"on": 1,
               "yirmi": 2,
               "otuz": 3,
               "kırk": 4,
               "elli": 5,
               "altmış": 6,
               "yetmiş": 7,
               "seksen": 8,
               "doksan": 9}

    onluk = {"yirmi": 2,
             "otuz": 3,
             "kırk": 4,
             "elli": 5,
             "altmış": 6,
             "yetmiş": 7,
             "seksen": 8,
             "doksan": 9}

    birlik_2 = {"": 0,
                "bir": 1,
                "iki": 2,
                "üç": 3,
                "dört": 4,
                "beş": 5,
                "altı": 6,
                "yedi": 7,
                "sekiz": 8,
                "dokuz": 9}

    for t in random.sample(range(0, 1000001), 1):
        if int(t) < 20:
            for z in random.sample(o1, 4):
                o2.append(z)

            o3.append(o2[0])

            soru = Label(text=str(o3[0]) + "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?",
                          font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if s1 == o3[0]:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for s1 in random.sample(o2, 1):
                but1 = Button(text=birlik_1[s1], command=yaz_1, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.3)

                o2.remove(s1)

            def yaz_2():
                if s2 == o3[0]:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for s2 in random.sample(o2, 1):
                but2 = Button(text=birlik_1[s2], command=yaz_2, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.4)

                o2.remove(s2)

            def yaz_3():
                if s3 == o3[0]:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for s3 in random.sample(o2, 1):
                but3 = Button(text=birlik_1[s3], command=yaz_3, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.5)

                o2.remove(s3)

            def yaz_4():
                if s4 == o3[0]:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for s4 in random.sample(o2, 1):
                but4 = Button(text=birlik_1[s4], command=yaz_4, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.6)

                o2.remove(s4)

        elif int(t) >= 19 and int(t) < 100:
            for w in random.sample(on_1, 4):
                o2.append(w)
            for t1 in random.sample(on_2, 4):
                o4.append(t1)

            o5[0][0] = o2[0]
            o5[0][1] = o4[0]

            a = onluk[o5[0][0]]
            a1 = birlik_2[o5[0][1]]

            o6[0][0] = a
            o6[0][1] = a1

            o5[1][0] = o2[1]
            o5[1][1] = o4[1]

            b = onluk[o5[1][0]]
            b1 = birlik_2[o5[1][1]]

            o6[1][0] = b
            o6[1][1] = b1

            o5[2][0] = o2[2]
            o5[2][1] = o4[2]

            c = onluk[o5[2][0]]
            c1 = birlik_2[o5[2][1]]

            o6[2][0] = c
            o6[2][1] = c1

            o5[3][0] = o2[3]
            o5[3][1] = o4[3]

            d = onluk[o5[3][0]]
            d1 = birlik_2[o5[3][1]]

            o6[3][0] = d
            o6[3][1] = d1

            print(o5)
            print(o6)

            soru = Label(text=str(o5[0][0]) + " " + str(o5[0][1]) +
                         "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?",
                          font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0]) == a and int(r1[1]) == a1:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o6, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]), command=yaz_1, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.3)
            o6.remove(r1)
            print(o6)

            def yaz_2():
                if int(r2[0]) == a and int(r2[1]) == a1:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o6, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]), command=yaz_2, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.4)
            o6.remove(r2)
            print(o6)

            def yaz_3():
                if int(r3[0]) == a and int(r3[1]) == a1:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o6, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]), command=yaz_3, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.5)
            o6.remove(r3)
            print(o6)

            def yaz_4():
                if int(r4[0]) == a and int(r4[1]) == a1:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o6, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]), command=yaz_4, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.6)
            o6.remove(r4)
            print(o6)

        elif int(t) == 100:
            for w in random.sample(on_1, 3):
                o2.append(w)
            for t1 in random.sample(on_2, 3):
                o4.append(t1)

            o5[0][0] = o2[0]
            o5[0][1] = o4[0]

            a = onluk[o5[0][0]]
            a1 = birlik_2[o5[0][1]]

            o6[0][0] = a
            o6[0][1] = a1

            o5[1][0] = o2[1]
            o5[1][1] = o4[1]

            b = onluk[o5[1][0]]
            b1 = birlik_2[o5[1][1]]

            o6[1][0] = b
            o6[1][1] = b1

            o5[2][0] = o2[2]
            o5[2][1] = o4[2]

            c = onluk[o5[2][0]]
            c1 = birlik_2[o5[2][1]]

            o6[2][0] = c
            o6[2][1] = c1

            o6[3][0] = "100"

            print(o5)
            print(o6)

            soru = Label(text="yüz" + "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0]) == 100:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o6, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]), command=yaz_1, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.3)
            o6.remove(r1)
            print(o6)

            def yaz_2():
                if int(r2[0]) == 100:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o6, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]), command=yaz_2, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.4)
            o6.remove(r2)
            print(o6)

            def yaz_3():
                if int(r3[0]) == 100:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o6, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]), command=yaz_3, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.5)
            o6.remove(r3)
            print(o6)

            def yaz_4():
                if int(r4[0]) == 100:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o6, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]), command=yaz_4, height=1, width=15, fg="white", bg="red",
                              font="FreeSans 20").place(relx=0.1, rely=0.6)
            o6.remove(r4)
            print(o6)

        elif int(t) > 100 and int(t) < 1000:
            for w in random.sample(yuz, 4):
                o2.append(w)
            for t1 in random.sample(on_3, 4):
                o4.append(t1)
            for t2 in random.sample(on_2, 4):
                o7.append(t2)

            o8[0][0] = o2[0]
            o8[0][1] = o4[0]
            o8[0][2] = o7[0]

            a = yuzluk[o8[0][0]]
            a1 = onluk_1[o8[0][1]]
            a2 = birlik_2[o8[0][2]]

            o9[0][0] = a
            o9[0][1] = a1
            o9[0][2] = a2

            o8[1][0] = o2[1]
            o8[1][1] = o4[1]
            o8[1][2] = o7[1]

            b = yuzluk[o8[1][0]]
            b1 = onluk_1[o8[1][1]]
            b2 = birlik_2[o8[1][2]]

            o9[1][0] = b
            o9[1][1] = b1
            o9[1][2] = b2

            o8[2][0] = o2[2]
            o8[2][1] = o4[2]
            o8[2][2] = o7[2]

            c = yuzluk[o8[2][0]]
            c1 = onluk_1[o8[2][1]]
            c2 = birlik_2[o8[2][2]]

            o9[2][0] = c
            o9[2][1] = c1
            o9[2][2] = c2

            o8[3][0] = o2[3]
            o8[3][1] = o4[3]
            o8[3][2] = o7[3]

            d = yuzluk[o8[3][0]]
            d1 = onluk_1[o8[3][1]]
            d2 = birlik_2[o8[3][2]]

            o9[3][0] = d
            o9[3][1] = d1
            o9[3][2] = d2

            print(o8)
            print(o9)

            soru = Label(text=str(o8[0][0]) + " " + str(o8[0][1]) + " " + str(o8[0][2]) +
                         "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0]) == a and int(r1[1]) == a1 and int(r1[2]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o9, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]) + str(r1[2]), command=yaz_1, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.3)
            o9.remove(r1)
            print(o9)

            def yaz_2():
                if int(r2[0]) == a and int(r2[1]) == a1 and int(r2[2]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o9, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]) + str(r2[2]), command=yaz_2, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.4)
            o9.remove(r2)
            print(o9)

            def yaz_3():
                if int(r3[0]) == a and int(r3[1]) == a1 and int(r3[2]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o9, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]) + str(r3[2]), command=yaz_3, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.5)
            o9.remove(r3)
            print(o9)

            def yaz_4():
                if int(r4[0]) == a and int(r4[1]) == a1 and int(r4[2]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o9, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]) + str(r4[2]), command=yaz_4, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.6)
            o9.remove(r4)
            print(o9)

        elif int(t) == 1000:
            for w in random.sample(yuz, 4):
                o2.append(w)
            for t1 in random.sample(on_3, 4):
                o4.append(t1)
            for t2 in random.sample(on_2, 4):
                o7.append(t2)

            o8[0][0] = o2[0]
            o8[0][1] = o4[0]
            o8[0][2] = o7[0]

            a = yuzluk[o8[0][0]]
            a1 = onluk_1[o8[0][1]]
            a2 = birlik_2[o8[0][2]]

            o9[0][0] = a
            o9[0][1] = a1
            o9[0][2] = a2

            o8[1][0] = o2[1]
            o8[1][1] = o4[1]
            o8[1][2] = o7[1]

            b = yuzluk[o8[1][0]]
            b1 = onluk_1[o8[1][1]]
            b2 = birlik_2[o8[1][2]]

            o9[1][0] = b
            o9[1][1] = b1
            o9[1][2] = b2

            o8[2][0] = o2[2]
            o8[2][1] = o4[2]
            o8[2][2] = o7[2]

            c = yuzluk[o8[2][0]]
            c1 = onluk_1[o8[2][1]]
            c2 = birlik_2[o8[2][2]]

            o9[2][0] = c
            o9[2][1] = c1
            o9[2][2] = c2

            o9[3][0] = "1000"

            print(o8)
            print(o9)

            soru = Label(text="bin" + "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0]) == 1000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o9, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]) + str(r1[2]), command=yaz_1, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.3)
            o9.remove(r1)
            print(o9)

            def yaz_2():
                if int(r2[0]) == 1000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o9, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]) + str(r2[2]), command=yaz_2, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.4)
            o9.remove(r2)
            print(o9)

            def yaz_3():
                if int(r3[0]) == 1000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o9, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]) + str(r3[2]), command=yaz_3, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.5)
            o9.remove(r3)
            print(o9)

            def yaz_4():
                if int(r4[0]) == 1000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o9, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]) + str(r4[2]), command=yaz_4, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.6)
            o9.remove(r4)
            print(o9)

        elif int(t) > 1000 and int(t) < 10000:
            for b in random.sample(bin_1, 4):
                o10.append(b)
            for w in random.sample(yuz_1, 4):
                o2.append(w)
            for t1 in random.sample(on_3, 4):
                o4.append(t1)
            for t2 in random.sample(on_2, 4):
                o7.append(t2)

            o11[0][0] = o10[0]
            o11[0][1] = o2[0]
            o11[0][2] = o4[0]
            o11[0][3] = o7[0]

            a3 = binlik[o11[0][0]]
            a = yuzluk_1[o11[0][1]]
            a1 = onluk_1[o11[0][2]]
            a2 = birlik_2[o11[0][3]]
            
            o12[0][0] = a3
            o12[0][1] = a
            o12[0][2] = a1
            o12[0][3] = a2

            o11[1][0] = o10[1]
            o11[1][1] = o2[1]
            o11[1][2] = o4[1]
            o11[1][3] = o7[1]

            b3 = binlik[o11[1][0]]
            b = yuzluk_1[o11[1][1]]
            b1 = onluk_1[o11[1][2]]
            b2 = birlik_2[o11[1][3]]
            
            o12[1][0] = b3
            o12[1][1] = b
            o12[1][2] = b1
            o12[1][3] = b2

            o11[2][0] = o10[2]
            o11[2][1] = o2[2]
            o11[2][2] = o4[2]
            o11[2][3] = o7[2]

            c3 = binlik[o11[2][0]]
            c = yuzluk_1[o11[2][1]]
            c1 = onluk_1[o11[2][2]]
            c2 = birlik_2[o11[2][3]]
            
            o12[2][0] = c3
            o12[2][1] = c
            o12[2][2] = c1
            o12[2][3] = c2

            o11[3][0] = o10[3]
            o11[3][1] = o2[3]
            o11[3][2] = o4[3]
            o11[3][3] = o7[3]

            d3 = binlik[o11[3][0]]
            d = yuzluk_1[o11[3][1]]
            d1 = onluk_1[o11[3][2]]
            d2 = birlik_2[o11[3][3]]
            
            o12[3][0] = d3
            o12[3][1] = d
            o12[3][2] = d1
            o12[3][3] = d2

            print(o11)
            print(o12)

            soru = Label(text=str(o11[0][0]) + " " + str(o11[0][1]) + " " + str(o11[0][2]) + " " +str(o11[0][3]) +
                         "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0]) == a3 and int(r1[1]) == a and int(r1[2]) == a1 and int(r1[3]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o12, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]) + str(r1[2]) + str(r1[3]), command=yaz_1, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.3)
            o12.remove(r1)
            print(o12)

            def yaz_2():
                if int(r2[0]) == a3 and int(r2[1]) == a and int(r2[2]) == a1 and int(r2[3]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o12, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]) + str(r2[2]) + str(r2[3]), command=yaz_2, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.4)
            o12.remove(r2)
            print(o12)

            def yaz_3():
                if int(r3[0]) == a3 and int(r3[1]) == a and int(r3[2]) == a1 and int(r3[3]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o12, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]) + str(r3[2]) + str(r3[3]), command=yaz_3, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.5)
            o12.remove(r3)
            print(o12)

            def yaz_4():
                if int(r4[0]) == a3 and int(r4[1]) == a and int(r4[2]) == a1 and int(r4[3]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o12, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]) + str(r4[2]) + str(r4[3]), command=yaz_4, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.6)
            o12.remove(r4)
            print(o12)

        elif int(t) == 10000:
            for b in random.sample(bin_1, 4):
                o10.append(b)
            for w in random.sample(yuz_1, 4):
                o2.append(w)
            for t1 in random.sample(on_3, 4):
                o4.append(t1)
            for t2 in random.sample(on_2, 4):
                o7.append(t2)

            o11[0][0] = o10[0]
            o11[0][1] = o2[0]
            o11[0][2] = o4[0]
            o11[0][3] = o7[0]

            a3 = binlik[o11[0][0]]
            a = yuzluk_1[o11[0][1]]
            a1 = onluk_1[o11[0][2]]
            a2 = birlik_2[o11[0][3]]
            
            o12[0][0] = a3
            o12[0][1] = a
            o12[0][2] = a1
            o12[0][3] = a2

            o11[1][0] = o10[1]
            o11[1][1] = o2[1]
            o11[1][2] = o4[1]
            o11[1][3] = o7[1]

            b3 = binlik[o11[1][0]]
            b = yuzluk_1[o11[1][1]]
            b1 = onluk_1[o11[1][2]]
            b2 = birlik_2[o11[1][3]]
            
            o12[1][0] = b3
            o12[1][1] = b
            o12[1][2] = b1
            o12[1][3] = b2

            o11[2][0] = o10[2]
            o11[2][1] = o2[2]
            o11[2][2] = o4[2]
            o11[2][3] = o7[2]

            c3 = binlik[o11[2][0]]
            c = yuzluk_1[o11[2][1]]
            c1 = onluk_1[o11[2][2]]
            c2 = birlik_2[o11[2][3]]
            
            o12[2][0] = c3
            o12[2][1] = c
            o12[2][2] = c1
            o12[2][3] = c2

            o12[3][0] = "10000"

            print(o11)
            print(o12)

            soru = Label(text="on bin" + "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0]) == 10000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o12, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]) + str(r1[2]) + str(r1[3]), command=yaz_1, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.3)
            o12.remove(r1)
            print(o12)

            def yaz_2():
                if int(r2[0]) == 10000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o12, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]) + str(r2[2]) + str(r2[3]), command=yaz_2, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.4)
            o12.remove(r2)
            print(o12)

            def yaz_3():
                if int(r3[0]) == 10000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o12, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]) + str(r3[2]) + str(r3[3]), command=yaz_3, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.5)
            o12.remove(r3)
            print(o12)

            def yaz_4():
                if int(r4[0]) == 10000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o12, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]) + str(r4[2]) + str(r4[3]), command=yaz_4, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.6)
            o12.remove(r4)
            print(o12)

        elif int(t) > 10000 and int(t) < 100000:
            for c in random.sample(on_bin, 4):
                o13.append(c)
            for b in random.sample(bin_1, 4):
                o10.append(b)
            for w in random.sample(yuz_1, 4):
                o2.append(w)
            for t1 in random.sample(on_3, 4):
                o4.append(t1)
            for t2 in random.sample(on_2, 4):
                o7.append(t2)

            o14[0][0] = o13[0]
            o14[0][1] = o10[0]
            o14[0][2] = o2[0]
            o14[0][3] = o4[0]
            o14[0][4] = o7[0]

            a4 = onluk_2[o14[0][0]]
            a3 = binlik_1[o14[0][1]]
            a = yuzluk_1[o14[0][2]]
            a1 = onluk_1[o14[0][3]]
            a2 = birlik_2[o14[0][4]]

            o15[0][0] = a4
            o15[0][1] = a3
            o15[0][2] = a
            o15[0][3] = a1
            o15[0][4] = a2

            o14[1][0] = o13[1]
            o14[1][1] = o10[1]
            o14[1][2] = o2[1]
            o14[1][3] = o4[1]
            o14[1][4] = o7[1]

            b4 = onluk_2[o14[1][0]]
            b3 = binlik_1[o14[1][1]]
            b = yuzluk_1[o14[1][2]]
            b1 = onluk_1[o14[1][3]]
            b2 = birlik_2[o14[1][4]]

            o15[1][0] = b4
            o15[1][1] = b3
            o15[1][2] = b
            o15[1][3] = b1
            o15[1][4] = b2

            o14[2][0] = o13[2]
            o14[2][1] = o10[2]
            o14[2][2] = o2[2]
            o14[2][3] = o4[2]
            o14[2][4] = o7[2]

            c4 = onluk_2[o14[2][0]]
            c3 = binlik_1[o14[2][1]]
            c = yuzluk_1[o14[2][2]]
            c1 = onluk_1[o14[2][3]]
            c2 = birlik_2[o14[2][4]]

            o15[2][0] = c4
            o15[2][1] = c3
            o15[2][2] = c
            o15[2][3] = c1
            o15[2][4] = c2

            o14[3][0] = o13[3]
            o14[3][1] = o10[3]
            o14[3][2] = o2[3]
            o14[3][3] = o4[3]
            o14[3][4] = o7[3]

            d4 = onluk_2[o14[3][0]]
            d3 = binlik_1[o14[3][1]]
            d = yuzluk_1[o14[3][2]]
            d1 = onluk_1[o14[3][3]]
            d2 = birlik_2[o14[3][4]]

            o15[3][0] = d4
            o15[3][1] = d3
            o15[3][2] = d
            o15[3][3] = d1
            o15[3][4] = d2                        

            print(o14)
            print(o15)

            soru = Label(text=str(o14[0][0]) + " " + str(o14[0][1]) + " " + str(o14[0][2]) + " " +str(o14[0][3]) + " " +str(o14[0][4]) +
                         "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0] == a4 and r1[1]) == a3 and int(r1[2]) == a and int(r1[3]) == a1 and int(r1[4]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o15, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]) + str(r1[2]) + str(r1[3]) + str(r1[4]), command=yaz_1, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.3)
            o15.remove(r1)
            print(o15)

            def yaz_2():
                if int(r2[0] == a4 and r2[1]) == a3 and int(r2[2]) == a and int(r2[3]) == a1 and int(r2[4]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o15, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]) + str(r2[2]) + str(r2[3]) + str(r2[4]), command=yaz_2, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.4)
            o15.remove(r2)
            print(o15)

            def yaz_3():
                if int(r3[0] == a4 and r3[1]) == a3 and int(r3[2]) == a and int(r3[3]) == a1 and int(r3[4]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o15, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]) + str(r3[2]) + str(r3[3]) + str(r3[4]), command=yaz_3, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.5)
            o15.remove(r3)
            print(o15)

            def yaz_4():
                if int(r4[0] == a4 and r4[1]) == a3 and int(r4[2]) == a and int(r4[3]) == a1 and int(r4[4]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o15, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]) + str(r4[2]) + str(r4[3]) + str(r4[4]), command=yaz_4, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.6)
            o15.remove(r4)
            print(o15)

        elif int(t) == 100000:
            for c in random.sample(on_bin, 4):
                o13.append(c)
            for b in random.sample(bin_1, 4):
                o10.append(b)
            for w in random.sample(yuz_1, 4):
                o2.append(w)
            for t1 in random.sample(on_3, 4):
                o4.append(t1)
            for t2 in random.sample(on_2, 4):
                o7.append(t2)

            o14[0][0] = o13[0]
            o14[0][1] = o10[0]
            o14[0][2] = o2[0]
            o14[0][3] = o4[0]
            o14[0][4] = o7[0]

            a4 = onluk_2[o14[0][0]]
            a3 = binlik_1[o14[0][1]]
            a = yuzluk_1[o14[0][2]]
            a1 = onluk_1[o14[0][3]]
            a2 = birlik_2[o14[0][4]]

            o15[0][0] = a4
            o15[0][1] = a3
            o15[0][2] = a
            o15[0][3] = a1
            o15[0][4] = a2

            o14[1][0] = o13[1]
            o14[1][1] = o10[1]
            o14[1][2] = o2[1]
            o14[1][3] = o4[1]
            o14[1][4] = o7[1]

            b4 = onluk_2[o14[1][0]]
            b3 = binlik_1[o14[1][1]]
            b = yuzluk_1[o14[1][2]]
            b1 = onluk_1[o14[1][3]]
            b2 = birlik_2[o14[1][4]]

            o15[1][0] = b4
            o15[1][1] = b3
            o15[1][2] = b
            o15[1][3] = b1
            o15[1][4] = b2

            o14[2][0] = o13[2]
            o14[2][1] = o10[2]
            o14[2][2] = o2[2]
            o14[2][3] = o4[2]
            o14[2][4] = o7[2]

            c4 = onluk_2[o14[2][0]]
            c3 = binlik_1[o14[2][1]]
            c = yuzluk_1[o14[2][2]]
            c1 = onluk_1[o14[2][3]]
            c2 = birlik_2[o14[2][4]]

            o15[2][0] = c4
            o15[2][1] = c3
            o15[2][2] = c
            o15[2][3] = c1
            o15[2][4] = c2

            o15[3][0] = "100000"

            print(o14)
            print(o15)

            soru = Label(text="yüz bin" + "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0]) == 100000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o15, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]) + str(r1[2]) + str(r1[3]) + str(r1[4]), command=yaz_1, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.3)
            o15.remove(r1)
            print(o15)

            def yaz_2():
                if int(r2[0]) == 100000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o15, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]) + str(r2[2]) + str(r2[3]) + str(r2[4]), command=yaz_2, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.4)
            o15.remove(r2)
            print(o15)

            def yaz_3():
                if int(r3[0]) == 100000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o15, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]) + str(r3[2]) + str(r3[3]) + str(r3[4]), command=yaz_3, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.5)
            o15.remove(r3)
            print(o15)

            def yaz_4():
                if int(r4[0]) == 100000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o15, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]) + str(r4[2]) + str(r4[3]) + str(r4[4]), command=yaz_4, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.6)
            o15.remove(r4)
            print(o15)

        elif int(t) > 100000 and int(t) < 1000000:
            for g in random.sample(yuz, 4):
                o16.append(g)
            for c in random.sample(on_bin_1, 4):
                o13.append(c)
            for b in random.sample(bin_1, 4):
                o10.append(b)
            for w in random.sample(yuz_1, 4):
                o2.append(w)
            for t1 in random.sample(on_3, 4):
                o4.append(t1)
            for t2 in random.sample(on_2, 4):
                o7.append(t2)

            o17[0][0] = o16[0]
            o17[0][1] = o13[0]
            o17[0][2] = o10[0]
            o17[0][3] = o2[0]
            o17[0][4] = o4[0]
            o17[0][5] = o7[0]

            a5 = yuzluk[o17[0][0]]
            a4 = onluk_1[o17[0][1]]
            a3 = binlik_1[o17[0][2]]
            a = yuzluk_1[o17[0][3]]
            a1 = onluk_1[o17[0][4]]
            a2 = birlik_2[o17[0][5]]

            o18[0][0] = a5
            o18[0][1] = a4
            o18[0][2] = a3
            o18[0][3] = a
            o18[0][4] = a1
            o18[0][5] = a2

            o17[1][0] = o16[1]
            o17[1][1] = o13[1]
            o17[1][2] = o10[1]
            o17[1][3] = o2[1]
            o17[1][4] = o4[1]
            o17[1][5] = o7[1]

            b5 = yuzluk[o17[1][0]]
            b4 = onluk_1[o17[1][1]]
            b3 = binlik_1[o17[1][2]]
            b = yuzluk_1[o17[1][3]]
            b1 = onluk_1[o17[1][4]]
            b2 = birlik_2[o17[1][5]]

            o18[1][0] = b5
            o18[1][1] = b4
            o18[1][2] = b3
            o18[1][3] = b
            o18[1][4] = b1
            o18[1][5] = b2

            o17[2][0] = o16[2]
            o17[2][1] = o13[2]
            o17[2][2] = o10[2]
            o17[2][3] = o2[2]
            o17[2][4] = o4[2]
            o17[2][5] = o7[2]

            c5 = yuzluk[o17[2][0]]
            c4 = onluk_1[o17[2][1]]
            c3 = binlik_1[o17[2][2]]
            c = yuzluk_1[o17[2][3]]
            c1 = onluk_1[o17[2][4]]
            c2 = birlik_2[o17[2][5]]

            o18[2][0] = c5
            o18[2][1] = c4
            o18[2][2] = c3
            o18[2][3] = c
            o18[2][4] = c1
            o18[2][5] = c2

            o17[3][0] = o16[3]
            o17[3][1] = o13[3]
            o17[3][2] = o10[3]
            o17[3][3] = o2[3]
            o17[3][4] = o4[3]
            o17[3][5] = o7[3]

            d5 = yuzluk[o17[3][0]]
            d4 = onluk_1[o17[3][1]]
            d3 = binlik_1[o17[3][2]]
            d = yuzluk_1[o17[3][3]]
            d1 = onluk_1[o17[3][4]]
            d2 = birlik_2[o17[3][5]]

            o18[3][0] = d5
            o18[3][1] = d4
            o18[3][2] = d3
            o18[3][3] = d
            o18[3][4] = d1
            o18[3][5] = d2                    

            print(o17)
            print(o18)

            soru = Label(text=str(o17[0][0]) + " " + str(o17[0][1]) + " " + str(o17[0][2]) + " " +str(o17[0][3]) + " " +str(o17[0][4]) + " " +str(o17[0][5]) +
                         "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0] == a5 and r1[1] == a4 and r1[2]) == a3 and int(r1[3]) == a and int(r1[4]) == a1 and int(r1[5]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o18, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]) + str(r1[2]) + str(r1[3]) + str(r1[4]) + str(r1[5]), command=yaz_1, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.3)
            o18.remove(r1)
            print(o18)

            def yaz_2():
                if int(r2[0] == a5 and r2[1] == a4 and r2[2]) == a3 and int(r2[3]) == a and int(r2[4]) == a1 and int(r2[5]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o18, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]) + str(r2[2]) + str(r2[3]) + str(r2[4]) + str(r2[5]), command=yaz_2, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.4)
            o18.remove(r2)
            print(o18)

            def yaz_3():
                if int(r3[0] == a5 and r3[1] == a4 and r3[2]) == a3 and int(r3[3]) == a and int(r3[4]) == a1 and int(r3[5]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o18, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]) + str(r3[2]) + str(r3[3]) + str(r3[4]) + str(r3[5]), command=yaz_3, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.5)
            o18.remove(r3)
            print(o18)

            def yaz_4():
                if int(r4[0] == a5 and r4[1] == a4 and r4[2]) == a3 and int(r4[3]) == a and int(r4[4]) == a1 and int(r4[5]) == a2:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o18, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]) + str(r4[2]) + str(r4[3]) + str(r4[4]) + str(r4[5]), command=yaz_4, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.6)
            o18.remove(r4)
            print(o18)

        elif int(t) == 1000000:
            for g in random.sample(yuz, 4):
                o16.append(g)
            for c in random.sample(on_bin_1, 4):
                o13.append(c)
            for b in random.sample(bin_1, 4):
                o10.append(b)
            for w in random.sample(yuz_1, 4):
                o2.append(w)
            for t1 in random.sample(on_3, 4):
                o4.append(t1)
            for t2 in random.sample(on_2, 4):
                o7.append(t2)

            o17[0][0] = o16[0]
            o17[0][1] = o13[0]
            o17[0][2] = o10[0]
            o17[0][3] = o2[0]
            o17[0][4] = o4[0]
            o17[0][5] = o7[0]

            a5 = yuzluk[o17[0][0]]
            a4 = onluk_1[o17[0][1]]
            a3 = binlik_1[o17[0][2]]
            a = yuzluk_1[o17[0][3]]
            a1 = onluk_1[o17[0][4]]
            a2 = birlik_2[o17[0][5]]

            o18[0][0] = a5
            o18[0][1] = a4
            o18[0][2] = a3
            o18[0][3] = a
            o18[0][4] = a1
            o18[0][5] = a2

            o17[1][0] = o16[1]
            o17[1][1] = o13[1]
            o17[1][2] = o10[1]
            o17[1][3] = o2[1]
            o17[1][4] = o4[1]
            o17[1][5] = o7[1]

            b5 = yuzluk[o17[1][0]]
            b4 = onluk_1[o17[1][1]]
            b3 = binlik_1[o17[1][2]]
            b = yuzluk_1[o17[1][3]]
            b1 = onluk_1[o17[1][4]]
            b2 = birlik_2[o17[1][5]]

            o18[1][0] = b5
            o18[1][1] = b4
            o18[1][2] = b3
            o18[1][3] = b
            o18[1][4] = b1
            o18[1][5] = b2

            o17[2][0] = o16[2]
            o17[2][1] = o13[2]
            o17[2][2] = o10[2]
            o17[2][3] = o2[2]
            o17[2][4] = o4[2]
            o17[2][5] = o7[2]

            c5 = yuzluk[o17[2][0]]
            c4 = onluk_1[o17[2][1]]
            c3 = binlik_1[o17[2][2]]
            c = yuzluk_1[o17[2][3]]
            c1 = onluk_1[o17[2][4]]
            c2 = birlik_2[o17[2][5]]

            o18[2][0] = c5
            o18[2][1] = c4
            o18[2][2] = c3
            o18[2][3] = c
            o18[2][4] = c1
            o18[2][5] = c2

            o18[3][0] = "1000000"

            print(o17)
            print(o18)

            soru = Label(text="bir milyon" + "                                                      ",
                         font="FreeSans 24").place(relx=0.4, rely=0.1)

            soru1 = Label(text="sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                         font="FreeSans 24").place(relx=0.3, rely=0.2)

            def yaz_1():
                if int(r1[0]) == 1000000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r1 in random.sample(o18, 1):
                print(r1)
                but1 = Button(text=str(r1[0]) + str(r1[1]) + str(r1[2]) + str(r1[3]) + str(r1[4]) + str(r1[5]), command=yaz_1, height=1, width=15, fg="white",
                              bg="red", font="FreeSans 20").place(relx=0.1, rely=0.3)
            o18.remove(r1)
            print(o18)

            def yaz_2():
                if int(r2[0]) == 1000000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r2 in random.sample(o18, 1):
                print(r2)
                but2 = Button(text=str(r2[0]) + str(r2[1]) + str(r2[2]) + str(r2[3]) + str(r2[4]) + str(r2[5]), command=yaz_2, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.4)
            o18.remove(r2)
            print(o18)

            def yaz_3():
                if int(r3[0]) == 1000000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r3 in random.sample(o18, 1):
                print(r3)
                but3 = Button(text=str(r3[0]) + str(r3[1]) + str(r3[2]) + str(r3[3]) + str(r3[4]) + str(r3[5]), command=yaz_3, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.5)
            o18.remove(r3)
            print(o18)

            def yaz_4():
                if int(r4[0]) == 1000000:
                    pygame.mixer.music.load("alkis.ogg")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("hata.ogg")
                    pygame.mixer.music.play()

            for r4 in random.sample(o18, 1):
                print(r4)
                but4 = Button(text=str(r4[0]) + str(r4[1]) + str(r4[2]) + str(r4[3]) + str(r4[4]) + str(r4[5]), command=yaz_4, height=1, width=15,
                              fg="white", bg="red", font="FreeSans 20").place(relx=0.1, rely=0.6)
            o18.remove(r4)
            print(o18)

hazirla = Button(text='HAZIRLA', command=okunus, height=3, width=10, fg="white", bg="red",
                 font="FreeSans 12").place(relx=0.1, rely=0.8)

buton = Button()
buton.config(text="ÇIKIŞ", command=root.destroy, height=3, width=10, fg="white", bg="red", font="FreeSans 12")
buton.place(relx=0.8, rely=0.8)

root.mainloop()
