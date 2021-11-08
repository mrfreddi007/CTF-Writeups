lorum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
streng2 = 'bagelarenotwholewheatsometimes'
streng1 = 'Lpthq jrvym!frpos"vmt!cpit-"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu"oebpth$eu"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp"oebptlw okvm vv#eljsxmp!g{$eb"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo"svojfhrt-"vynu"lr dwota!sxm phimcjc#hetguynu"pslmkw$aokp$ie"hwt!ndfoswp2'

def main():
    decoding = decode(streng1)
    print(decoding + "\n")
    if decoding == lorum:
        print("Decoding worked\n")
    print("Flag = dam{" + encode(streng2) + "}")

def decode(text):
    a = 0
    b=0
    decoded = ""
    for i in text:
        decoded = decoded + (chr(ord(text[a])-b))
        a = a+1
        if b>=4:    
            b = 0
        else:
            b = b + 1
    return(decoded)

def encode(text):
    a = 0
    b=0
    lorumenc=""
    for i in text:
        lorumenc = lorumenc + (chr(ord(text[a])+b))
        a = a+1
        if b>=4:    
            b = 0
        else:
            b = b + 1
    return(lorumenc)
    



if __name__ == "__main__":
    main()

