def muchal_nomi():
    yil = int(input("Tug`ilgan yilingizni kiriting\n>>>"))
    m = yil % 12
    if m == 4:
        print("Sizning muchalingiz SICHQON ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nGalileo Galiley, Jorj Vashington, Uilliyam Shekspir, Amir Temur")
    if m == 5:
        print("Sizning muchalingiz SIGIR ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nIogann Guttenberg, Napoleon I, Adolf Gitler, Iogann Sebastian Bax")
    if m == 6:
        print("Sizning muchalingiz YO`L`BARS ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nKarl Marks, Ludvig van Betxoven, Iosif Stalin, Jorj Hegel")
    if m == 7:
        print("Sizning muchalingiz QUYON ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nAlbert Enshteyn, Martin Lyuter, Adam Smit, Zahiriddin Muhammad Bobur")
    if m == 8:
        print("Sizning muchalingiz BALIQ ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nKonstantin I, Jeyms Uatt, Zigmund Freyd, Janna d'Ark")
    if m == 9:
        print("Sizning muchalingiz ILON ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nUmar ibn Xattob, Nikolay Kopernik, Rene Dekart, Uilgelm Rentgen")
    if m == 10:
        print("Sizning muchalingiz OT ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nIsaak Nyuton, Lenin, Chingizxon, Neil Armstrong")
    if m == 11:
        print("Sizning muchalingiz QO`Y ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nXristofor Kolumb, Tomas Edison, Aleksandr Graham Bell, Ernest Rezerford")
    if m == 0:
        print("Sizning muchalingiz MAYMUN ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nAl-Xorazmiy, Vilgelm II, Hans Hoffmann")
    if m == 1:
        print("Sizning muchalingiz TOVUQ ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nSuy Ven Di, Al-Beruniy")
    if m == 2:
        print("Sizning muchalingiz IT ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nSay Lun, Volter, Vinston Cherchill")
    if m == 3:
        print("Sizning muchalingiz TO`NG`IZ ekan. Sizning muchalingizda tug`ilgan mashxur shaxslar\nOtto fon Bismark, Maykl Faradey, Leonard Eyler, Genri Ford")
    return yil
