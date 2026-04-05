import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import requests

# ─────────────────────────────────────────────
# 1. Email OTP Function
# ─────────────────────────────────────────────
def send_email(receiver_email):
    otp = random.randint(1000, 9999)
    sender_email = "chalaksetu@gmail.com"
    sender_password = "cdxa ztyl jjig zkev"

    subject = "ChalakSetu OTP Verification"
    body = (
        f"Namaste!\n\n"
        f"Aapka ChalakSetu OTP hai: {otp}\n"
        f"Yeh OTP 10 minutes tak valid rahega.\n\n"
        f"- ChalakSetu Team"
    )

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        notice = f"OTP sent successfully to {receiver_email}"
    except Exception as e:
        notice = f"Failed to send email. Error: {e}"

    return otp, notice

# ─────────────────────────────────────────────
# 2. Location Functions (unchanged)
# ─────────────────────────────────────────────
def get_my_location():
    response = requests.get("https://ipinfo.io")
    data = response.json()
    loc = data.get("loc")
    if loc:
        lat, lng = map(float, loc.split(","))
        return lat, lng
    return None

def get_osm_mechanics(lat, lon, radius=10000):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
      node["shop"="car_repair"](around:{radius},{lat},{lon});
      way["shop"="car_repair"](around:{radius},{lat},{lon});
      relation["shop"="car_repair"](around:{radius},{lat},{lon});
    );
    out center;
    """
    resp = requests.get(overpass_url, params={'data': query})
    if resp.status_code != 200:
        return []

    elements = resp.json().get('elements', [])
    mechanics = []
    for el in elements:
        name = el.get('tags', {}).get('name', 'Unnamed Mechanic')
        lat = el.get('lat') or el.get('center', {}).get('lat')
        lon = el.get('lon') or el.get('center', {}).get('lon')
        mechanics.append({'name': name, 'latitude': lat, 'longitude': lon})
    return mechanics[:4]

def near_mechnics(city, df):
    if city == "My Current Location":
        coords = get_my_location()
        if not coords:
            return ["Could not determine your location."]
        lat, lon = coords
    else:
        lat = float(df[df['City Name'] == city]['Latitude'])
        lon = float(df[df['City Name'] == city]['Longitude'])

    mechs = get_osm_mechanics(lat, lon)
    if not mechs:
        return ["No mechanic shops found nearby."]
    return [f"{i+1}. {m['name']} at ({m['latitude']}, {m['longitude']})"
            for i, m in enumerate(mechs)]
