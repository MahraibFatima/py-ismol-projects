import emoji

def print_weather_emoji(temperature, is_raining):
    if temperature > 30:
        if is_raining:
            print(emoji.emojize(":cloud_with_rain: It's hot and raining!"))
        else:
            print(emoji.emojize(":sunny: It's hot and sunny!"))
    elif 20 <= temperature <= 30:
        if is_raining:
            print(emoji.emojize(":sun_behind_rain_cloud: It's warm and raining."))
        else:
            print(emoji.emojize(":partly_sunny: It's warm and partly cloudy."))
    elif temperature < 20:
        if is_raining:
            print(emoji.emojize(":cloud_with_rain: It's cool and raining."))
        else:
            print(emoji.emojize(":wind_face: It's cool and windy."))