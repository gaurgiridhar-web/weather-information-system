import os
import requests
import streamlit as st

st.set_page_config(
    page_title="Weather Information System",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Weather Information System")
st.write("Find current weather information for a city anywhere in the world.")

# The API key is stored as an environment variable, not inside the source code.
API_KEY = os.getenv("OPENWEATHER_API_KEY", "").strip()

city = st.text_input("Enter a city name", placeholder="For example: Delhi")

if st.button("Get Weather", type="primary", use_container_width=True):
    if not city.strip():
        st.warning("Please enter a city name.")
    elif not API_KEY:
        st.error(
            "The weather API key has not been configured. "
            "Ask the project administrator to add OPENWEATHER_API_KEY."
        )
    else:
        endpoint = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city.strip(),
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            with st.spinner("Getting current weather..."):
                response = requests.get(endpoint, params=params, timeout=15)

            if response.status_code == 200:
                weather = response.json()
                main = weather["main"]
                condition = weather["weather"][0]
                wind = weather.get("wind", {})

                st.success(
                    f"Weather found for {weather['name']}, "
                    f"{weather['sys'].get('country', '')}."
                )

                icon_code = condition.get("icon")
                if icon_code:
                    st.image(
                        f"https://openweathermap.org/img/wn/{icon_code}@2x.png",
                        width=90
                    )

                st.subheader(condition.get("description", "Weather").title())

                col1, col2 = st.columns(2)
                col1.metric("Temperature", f"{main.get('temp', 'N/A')} °C")
                col2.metric("Feels like", f"{main.get('feels_like', 'N/A')} °C")

                col3, col4 = st.columns(2)
                col3.metric("Humidity", f"{main.get('humidity', 'N/A')}%")
                col4.metric("Wind speed", f"{wind.get('speed', 'N/A')} m/s")

                st.caption(
                    "Data provided by OpenWeatherMap. "
                    "This app displays current conditions, not a forecast."
                )

            elif response.status_code == 404:
                st.error("City not found. Check the spelling and try again.")
            elif response.status_code == 401:
                st.error(
                    "The API key was rejected. Check that it is correct "
                    "and has been activated."
                )
            elif response.status_code == 429:
                st.error("The weather service request limit was reached. Try later.")
            else:
                st.error(
                    f"The weather service returned an error "
                    f"(HTTP {response.status_code}). Please try again."
                )

        except requests.exceptions.Timeout:
            st.error("The weather service took too long to respond. Try again.")
        except requests.exceptions.RequestException:
            st.error("Could not connect to the weather service. Check your internet.")
        except (KeyError, TypeError, ValueError):
            st.error("The weather service returned data in an unexpected format.")

st.divider()
st.caption("Student project | Python • Streamlit • OpenWeatherMap • Microsoft Azure")
