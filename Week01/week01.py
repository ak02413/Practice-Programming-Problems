def framed(string_lst):
    max_len = len(max(string_lst, key = len))
    print((max_len+2) * "*")
    for i in string_lst:
        print("*" + i + " " * (max_len - len(i)) + "*")
    print((max_len+2) * "*")

def beer_bottles():
    lyric0 = "bottles"
    lyric1 = "of beer on the wall. Take one down, and pass it around.\n"
    lyric2 = "of beer on the wall.\n"
    lyric3 = "Go to the store and buy some more, 99 bottles of beer on the wall."
    beers = 99;
    for i in range(0, 100):
        if (beers - i) >= 1:
            if (beers - i) == 1:
                print((beers - i), lyric0[:-1], lyric1 + str((beers - i - 1)), lyric0[:-1], lyric2)
            else:           
                print((beers - i), lyric0, lyric1 + str((beers - i - 1)), lyric0, lyric2)    
        else:
            print("No more", lyric2 + lyric3)

