import def2
ty=def2.muchal_nomi()
hy=input("Oldingi va kelasi muchalingiz qachon ekanligini bilmoqchi bo`lsangiz hozirgi yilni kiriting\n>>>")
if len(hy)==0:
    hy=2022
else:
    hy=int(hy)
y=hy-ty
omy=hy-(y%12)
kmy=omy+12

if omy==hy:

    print(f'Bu yil sizning muchalingiz.\nKeyingi muchalingiz {kmy}-yilda.')
else:
    print(f'Oldingi muchal yilingiz {omy}-yilda edi.\nKeyingi muchalingiz {kmy}-yilda keladi.')


