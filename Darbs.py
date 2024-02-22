def lasit_datni():
    try:
        with open("teksts1.txt", 'r', encoding='utf8') as datne:
            saturs=datne.read()
            print(saturs)
        with open("teksts1.txt",'w', encoding='utf8')as ff:
            ff.write("šodien iešu uz veikalu un nopirkšu")
        with open("teksts1.txt",'a', encoding='utf8')as f:
            f.write(",augļus,,dārzeņus,saldumus")
         
    except FileNotFoundError:
        print("datne nav atrasta!")
if __name__=="__main__":
  lasit_datni()