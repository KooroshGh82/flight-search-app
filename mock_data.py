# import requests
# from bs4 import BeautifulSoup

# def crawl_tours(url: str):
#     headers = {"User-Agent": "Mozilla/5.0"}
#     resp = requests.get(url, headers=headers)
#     soup = BeautifulSoup(resp.text, "html.parser")

#     tours = []

#     for card in soup.select(".tour"):
#         title = card.select_one(".title").text.strip()
#         price = card.select_one(".price").text.strip()
#         duration = card.select_one(".duration").text.strip()

#         tours.append({
#             "title": title,
#             "price": price,
#             "duration": duration,
#         })

#     return tours

# tours = crawl_tours("https://nahalgasht.com/tours/foreign/")
# print(tours)



MOCK_TOURS = [
    {
        "origin": "تهران",
        "destination": "مشهد",
        "price": 2200000,
        "airline": "قشم‌ایر",
        "description": "تور اقتصادی تهران به مشهد با پرواز صبحگاهی",
        "source": "mrbilit.com",
        "url": "https://www.mrbilit.com/tour/tehran-mashhad-1"
    },
    {
        "origin": "تهران",
        "destination": "شیراز",
        "price": 2500000,
        "airline": "ایران‌ایر",
        "description": "پرواز مستقیم تهران به شیراز مناسب سفر تفریحی",
        "source": "alibaba.ir",
        "url": "https://www.alibaba.ir/tour/tehran-shiraz-1"
    },
    {
        "origin": "اصفهان",
        "destination": "کیش",
        "price": 3900000,
        "airline": "ماهان",
        "description": "تور پروازی اصفهان به کیش با خدمات ویژه",
        "source": "flytoday.ir",
        "url": "https://www.flytoday.ir/tour/isfahan-kish-1"
    },
    {
        "origin": "تبریز",
        "destination": "مشهد",
        "price": 2800000,
        "airline": "آتا",
        "description": "پرواز تبریز به مشهد با توقف کوتاه",
        "source": "alibaba.ir",
        "url": "https://www.alibaba.ir/tour/tabriz-mashhad-1"
    },
    {
        "origin": "شیراز",
        "destination": "تهران",
        "price": 2100000,
        "airline": "ایران‌ایر",
        "description": "پرواز برگشت شیراز به تهران مناسب سفر کاری",
        "source": "mrbilit.com",
        "url": "https://www.mrbilit.com/tour/shiraz-tehran-1"
    },
    {
        "origin": "مشهد",
        "destination": "کیش",
        "price": 4200000,
        "airline": "کیش‌ایر",
        "description": "تور لوکس مشهد به کیش با اقامت اختیاری",
        "source": "flytoday.ir",
        "url": "https://www.flytoday.ir/tour/mashhad-kish-1"
    },
    {
        "origin": "اهواز",
        "destination": "تهران",
        "price": 2000000,
        "airline": "زاگرس",
        "description": "پرواز اهواز به تهران اقتصادی",
        "source": "alibaba.ir",
        "url": "https://www.alibaba.ir/tour/ahvaz-tehran-1"
    },
    {
        "origin": "رشت",
        "destination": "مشهد",
        "price": 2700000,
        "airline": "ماهان",
        "description": "پرواز رشت به مشهد با ایرلاین ماهان",
        "source": "mrbilit.com",
        "url": "https://www.mrbilit.com/tour/rasht-mashhad-1"
    },
    {
        "origin": "تهران",
        "destination": "قشم",
        "price": 3600000,
        "airline": "قشم‌ایر",
        "description": "تور پروازی تهران به قشم مناسب سفر خانوادگی",
        "source": "flytoday.ir",
        "url": "https://www.flytoday.ir/tour/tehran-qeshm-1"
    },
    {
        "origin": "کرمان",
        "destination": "مشهد",
        "price": 3100000,
        "airline": "ایران‌ایر",
        "description": "پرواز کرمان به مشهد ویژه زائران",
        "source": "alibaba.ir",
        "url": "https://www.alibaba.ir/tour/kerman-mashhad-1"
    }
]
