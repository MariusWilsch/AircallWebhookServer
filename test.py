import requests

url = "https://production-fra-555773567328-web-recordings.s3.eu-central-1.amazonaws.com/companies/432833/recordings/2024/03/17/1710682317586-CAbf8d999ca4373ae33c1e707d9ff0a56f-RE049afe964c6976d03c76734f35f614d3.mp3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYCZVPUFQPU6IBRUS%2F20240317%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240317T133246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjaoBslWrX2WHudipmfT6Fjepk%2BTgdAhzJ%2FjzqeRnHYwIhAKqsfS1O35pqR53Il6yHqYoouyayquSAT19P7dBLogPWKo4ECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQAxoMNTU1NzczNTY3MzI4IgwgKUK8K3wgLBlkGzUq4gNGch8Cj7yYGg%2FlOlw1%2Bq5GLVlc1%2BnfxBRKRitY%2Fkmrp6vljDFwpmbWvmC8LZFlxOjkfKTTpGmX3p7L%2B71IpWlO4XpOqulP%2F1TCIG7Miiy%2FG4NNTmSiZS8Sk1L8%2F5ix%2F95JVylkdjEp90MOtDU8PWxJvrrnBl7v8mucgIPQrSKH8NWhK9LrtrWpineheR3PS%2BS807OsR4CaJpA42XJMu0a9SoWdTl8tX2KYt8pr0Rz%2B0PnIFAERyr%2FIR3%2FmxE9tIwL6t4YRbXZ8xyfAXdETkA0iBxVoBTMfY3lyOt7jANmVcmZbECfJ9RdqGWFsAleukatbzRo6u3guu5Kst%2BewZgXS68OStX4qDoj7khH4UbMauMWpuq7X7yK9J%2B%2Bc3UKLYW1B6SYy2wAKGa16NUA9R6igVF%2BJGihlyMFpNFfanrsIZMGnwUBwlxxvm9dZui9WtV2CkcuJ9u%2F%2BzszkYnUrxvMPfPP%2F9calXfz%2Bw%2FxZkBf9TeBhnqBlT2Y4soIWLDMoWBuMx2Za9tIDBQyOYfy1DtN9UVZIjM5lHoSz2msBv2beCZukbVIoGBmyvYh0XkMRZysz%2FPhIbwF9YuQmOlLTi3G%2FTi76LPOeAaZqndBNONMpGe3gAc7PH1vd0Rn05RRhGfRKKTDb39uvBjqkAQZXnx%2Bq9Fc64611YYwJEqiFP5Cyp%2BRq1Mp7%2FDHVd%2BmtWIN6wSzwsjyeeGM%2Fd%2Bokrfxgpzaxt8dkzpTCUd8VEIMTbk0zy%2Fc0UgZBPylDI0Iz91p3YdzoTYeUbI%2FWhA5Sc6hjMxqVDPKrmZONi7hVB5shxxeJjNXPYbcP8EUsHm4FYz5ahmnGepeDKxee0PPztJDMdKmC6ErCblvpBBEMs%2Fyia5ZP&X-Amz-SignedHeaders=host&X-Amz-Signature=9f8ae504f15f5f9cd7d45787d90d281f503be8a854c1bd472239c5aed34f0407"

response = requests.get(url)
if response.status_code == 200:
    with open("downloaded_file.mp3", "wb") as file:
        file.write(response.content)
        print("File downloaded successfully.")
else:
    print("Failed to download the file.")
