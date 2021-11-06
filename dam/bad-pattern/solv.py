streng2 = 'bagelarenotwholewheatsometimes'
streng1 = 'Lpthq jrvym!frpos"vmt!cpit-"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu"oebpth$eu"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp"oebptlw okvm vv#eljsxmp!g{$eb"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo"svojfhrt-"vynu"lr dwota!sxm phimcjc#hetguynu"pslmkw$aokp$ie"hwt!ndfoswp2'
a = 0
b=0
strengen=""
#streng = streng.replace("!"," ")
for i in streng1:
    c = streng1[a]
    streng1[a] = c.replace(streng1[a],str(chr(ord(streng1[a])-b)))
    #print(ord(streng[a]))
    strengen = strengen + (chr(ord(streng2[a])+b))
    print(chr(ord(streng2[a])+b))
    a = a+1
    if b>=4:    
        b = 0
    else:
        b = b + 1
        
    

print(streng1)
print("dam{" + strengen + "}")
