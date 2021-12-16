import requests
from requests.structures import CaseInsensitiveDict

iconDict = {

	"01":"☀️",
	"02":"⛅",
	"03":"🌥️",
	"04":"☁️",
	"09":"🌧️",
	"10":"🌦️",
	"11":"⛈️",
	"13":"❄️",
	"14":"🌫️"	
 }


def main():
	url = "http://api.openweathermap.org/data/2.5/weather?q=bergamo&appid=4c1ae3c1a2cbd1c3ff74c66b9305557a&units=metric"

	headers = CaseInsensitiveDict()
	headers["Authorization"] = "Bearer 4c1ae3c1a2cbd1c3ff74c66b9305557a"

	resp = requests.get(url, headers=headers)

	respCode = resp.status_code

	if (respCode == 200):
		respData = resp.json()

		print(str(respData['main']['temp'])[:4] + "°C")
		return;
	print(f"Error: {respCode}")

if __name__ == "__main__":
	main()
