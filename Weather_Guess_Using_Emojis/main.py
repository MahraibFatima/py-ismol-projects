import WeatherGuessWithEmojis.py

temperature = input("Enter the temperature: ")
is_raining = (input("Is it raining? (yes/no): ").lower() == "yes")

print_weather_emoji(temperature, is_raining)