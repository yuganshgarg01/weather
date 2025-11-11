import requests
import streamlit as st

st.set_page_config(page_title="Weather Chatbot", layout="centered")

st.title("🌦️ Simple Weather Chatbot (No API Key Needed)")
st.caption("Type a city name to see its current weather instantly.")

# Input field for city name only
city = st.text_input("Enter city name", placeholder="e.g. Bhopal")

if st.button("Get Weather"):
    if not city:
        st.warning("Please enter a city name.")
    else:
        try:
            # Using the free wttr.in API (no key required)
            url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Extract main weather info
            current = data["current_condition"][0]
            temp_c = current["temp_C"]
            feels_like = current["FeelsLikeC"]
            humidity = current["humidity"]
            pressure = current["pressure"]
            desc = current["weatherDesc"][0]["value"]

            # Show results
            st.success(f"Weather in {city}: {desc}")
            st.write(f"🌡️ Temperature: {temp_c} °C (Feels like {feels_like} °C)")
            st.write(f"💧 Humidity: {humidity}% | ⬇️ Pressure: {pressure} hPa")

            # Explain the output
            with st.expander("How I got this info"):
                st.markdown(
                    "This data comes from the **wttr.in** weather service — "
                    "a free, no-key API that uses real-time global weather data.\n"
                    "- `temp_C` shows the temperature in Celsius.\n"
                    "- `FeelsLikeC` estimates comfort temperature.\n"
                    "- `humidity` and `pressure` provide extra context."
                )

        except Exception as e:
            st.error("❌ Could not fetch weather. Please check your internet connection or city name.")

st.markdown("---")
st.caption("Minimal Streamlit app • Powered by wttr.in")

