from not_conditionals import case0_if
from not_conditionals import case01_dict
from not_conditionals import case1_get
from not_conditionals import case2_noif
from not_conditionals import case4_hof



def show(obj):
    try:
        print(obj.return_cost())
    except NameError as e:
        print(e)


if __name__ == "__main__":
    print("====== Case if =======")
    show(case0_if.Spotify('single'))
    show(case0_if.Spotify('duo'))
    show(case0_if.Spotify('family'))
    show(case0_if.Spotify('university'))
    show(case0_if.Spotify('brazil'))
    show(case0_if.Spotify('Brazil'))
    print("\n\n====== Case dict =======")
    show(case01_dict.Spotify('single'))
    show(case01_dict.Spotify('duo'))
    show(case01_dict.Spotify('family'))
    show(case01_dict.Spotify('university'))
    show(case01_dict.Spotify('brazil'))
    show(case01_dict.Spotify('Brazil'))
    print("\n\n====== Case get =======")
    show(case1_get.Spotify('single'))
    show(case1_get.Spotify('duo'))
    show(case1_get.Spotify('family'))
    show(case1_get.Spotify('university'))
    show(case1_get.Spotify('brazil'))
    show(case1_get.Spotify('Brazil'))    
    print("\n\n====== Case no if =======")
    show(case2_noif.Spotify('single'))
    show(case2_noif.Spotify('duo'))
    show(case2_noif.Spotify('family'))
    show(case2_noif.Spotify('university'))
    show(case2_noif.Spotify('brazil'))
    show(case2_noif.Spotify('Brazil'))
    print("\n\n====== Design Pattner HOF =======")
    show(case4_hof.Spotify('single'))
    show(case4_hof.Spotify('duo'))
    show(case4_hof.Spotify('family'))
    show(case4_hof.Spotify('university'))
    show(case4_hof.Spotify('brazil'))
    show(case4_hof.Spotify('Brazil'))