def lasit_datni():
    pass
    try:
       with open("teksts.txt", 'r', encoding='utf8') as datne:
            saturs=datne.read()
            print(type(saturs))
            print(saturs)

    except FileNotFoundError:
        print("datne nav atrasta!")


if __name__=="__main__":
  lasit_datni()

