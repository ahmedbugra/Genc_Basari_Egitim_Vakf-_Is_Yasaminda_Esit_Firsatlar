from requests import get
from pprint import pprint

endpoint = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=9db70862e4fa4ac6b49437eca63053a5"
response = get(url = endpoint)

data = response.json()
pprint(data)

print("\n----------------------------------------------------------------------------------------------------\n")

def find_name():
    author_name = input("Lütfen Yazar İsmi Giriniz: ")
    found_in_authors = False

    for i in data["articles"]:
        if i["author"] == author_name:
            pprint(i)
            found_in_authors = True 

    if not found:
            print("Böyle Bir Yazar Bulunamadı")

def find_date():
    publish_date = input("Lütfen Bir Tarih Giriniz (YYYY-AA-GG): ")
    found_in_dates = False

    for j in data["articles"]:
        if j["publishedAt"][0:10] == publish_date:
            pprint(j)
            found_in_dates = True

    if not found_in_dates:
        print("Aranan Tarihte Bir Makale Bulunamadı")



def program():
    process = input("Lütfen Yapmak İstediğiniz İşlemi Giriniz (Oluştur, Ara, Güncelle, Sil): ")

    if process == "Oluştur":        
        author_input = input("Lütfen Yazar İsmi Giriniz: ")
        title_input = input("Lütfen Başlık Giriniz: ")
        description_input = input("Lütfen Bir Açıklama Giriniz: ")

        dictionary_input = {
            "author" : author_input, 
            "title" : title_input, 
            "description" : description_input}

        data["articles"].append(dictionary_input)
        pprint(data["articles"])
        
        print("\n---------- Yeni Makale Eklendi ----------")
        

    if process == "Ara":
        criteria = input("Lütfen Arama Kriteri Giriniz (Yazar, Tarih): ")
        
        if criteria == "Yazar":
            find_name()

        if criteria == "Tarih":
            find_date()

    if process == "Güncelle":
        update_input = int(input("Lütfen Güncellemek İstediğiniz Makale Numarasını Giriniz (1-5): "))
        
        update_author_input = input("Güncel Yazar İsmi: ")
        update_title_input = input("Güncel Başlık: ")
        update_description_input = input("Güncel Açıklama: ")
        
        data["articles"][update_input - 1].update({
                "author": update_author_input,
                "title": update_title_input,
                "description": update_description_input
            })

        pprint(data["articles"])

        print("\n---------- Makale Güncellendi ----------")

    if process == "Sil":
        delete_input = int(input("Lütfen Silmek İstediğiniz Makale Numarası Giriniz (1-5): "))
        del data["articles"][delete_input - 1]

        pprint(data["articles"])

        print("\n---------- Makale Silindi ----------")

program()