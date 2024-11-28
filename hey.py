import streamlit as st
from PIL import Image
import json

# Set up the sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ("Home", "Know About the Crop", "Know About the Disease", "Buy Pesticides"))

# Title of the web app
st.markdown(
    """
    <style>
    .title {
        font-family: 'Brush Script MT', cursive;
        font-size: 50px;
        color: #FF0000; /* Red color */
        text-align: center;
        margin: 20px 0;
    }
    </style>
    <h1 class="title">Dr. Tomato</h1>
    """,
    unsafe_allow_html=True,
)

# Define the function to load crop information from JSON
def load_crop_info(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)  # Load the JSON data from the file

        # Extracting tomato crop information from the loaded JSON data
        tomato_crop_info = data.get("tomato_crop", {})
        
        return {
            "fertilizers": tomato_crop_info.get("fertilizers", []),
            "irrigation": tomato_crop_info.get("irrigation", []),
            "soil_type": tomato_crop_info.get("soil_type", [])
        }
    except FileNotFoundError:
        st.error(f"Error: The file {json_file} was not found.")
        return {}
    except json.JSONDecodeError:
        st.error(f"Error: Failed to decode JSON from the file {json_file}.")
        return {}
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return {}
# run_script.py
import subprocess

def get_output_from_script(image):
    result = subprocess.run(
        ['python', 'script_to_run.py'],
         input=image,   # Command to run the script
        capture_output=True,             # Capture stdout and stderr
        text=True                        # Return output as a string
    )
    return result.stdout.strip() 
# Function to detect disease (Placeholder)
def detect_disease(image):
  return {f"disease": "Jassid and Mite"}





# Function to fetch pesticide information (Placeholder)
def fetch_pesticide_info(disease_name):
    # Dictionary to store details for each disease with two pesticides
 pesticide_data = {
    "Jassid and Mite": [
        {
            "pesticide_name": "Chipku Pure Cold Pressed Water Soluble Neem Oil Concentrate For Plants & Garden 250ml With FREE Measuring Cup",
            "image_url": "https://m.media-amazon.com/images/I/61lrDVR3utL._SX679_.jpg",
            "buy_link": "https://www.amazon.in/Chipku-Pressed-Soluble-Plants-Garden/dp/B08VRJLGL9",
            "price": 299
        },
        {
            "pesticide_name": "Naturalis Essence of Nature Organic Neem Oil Pesticide (Water Soluble) For Spray on Plants & Garden 250ml",
            "image_url": "https://m.media-amazon.com/images/I/51vmyZS2hfL._SY879_.jpg",
            "buy_link": "https://www.amazon.in/Naturalis-Essence-Nature-Organic-Pesticide/dp/B07WSDC78S",
            "price": 851
        }
    ],
    "Leaf Miner": [
        {
            "pesticide_name": "UGAOO MealyMagic Mealy Bug & Fungus Killer Spray For Plants - 100% Herbal Actives & No Chemicals",
            "image_url": "https://m.media-amazon.com/images/I/51P0pvNnoFL._SX679_.jpg",
            "buy_link": "https://www.amazon.in/UGAOO-MealyMagic-Fungus-Killer-Plants/dp/B0CPJHN86D",
            "price": 349
        },
        {
            "pesticide_name": "Naturalis Essence of Nature Organic Neem Oil Pesticide (Water Soluble) For Spray on Plants & Garden 250ml",
            "image_url": "https://m.media-amazon.com/images/I/51vmyZS2hfL._SY879_.jpg",
            "buy_link": "https://www.amazon.in/Naturalis-Essence-Nature-Organic-Pesticide/dp/B07WSDC78S",
            "price": 851
        }
    ],
    "Mite": [
        {
            "pesticide_name": "THE WET TREE Bio Meta Cure (Metarhizium Anisopliae Liquid)",
            "image_url": "https://m.media-amazon.com/images/I/517F66h15lL._SX522_.jpg",
            "buy_link": "https://www.amazon.in/WET-TREE-Metarhizium-Anisopliae-Insecticide/dp/B0D6R2S5TT",
            "price": 270
        },
        {
            "pesticide_name": "Sansar Agro® Mealy Bug Remover Spray, Premium Essential Liquid Spray For Complete Removal Of Mealy Bugs From Plants",
            "image_url": "https://m.media-amazon.com/images/I/71iTTu-bHXL._SX522_.jpg",
            "buy_link": "https://www.amazon.in/Remover-Premium-Essential-complete-removal/dp/B09H6TVDYF",
            "price": 580
        }
    ],
    "Nitrogen and Potassium Defficiency": [
        {
            "pesticide_name": "PREPLE Urea Fertilizer Neem Coated Water Soluble for Vegetables, Flowers, Fruits Plants, Maximum Production, Ideal for Home, Terrace, and Outdoor Gardens",
            "image_url": "https://m.media-amazon.com/images/I/71l6y+z2OhL._SY500_.jpg",
            "buy_link": "https://www.amazon.in/PREPLE-Fertilizer-Soluble-Vegetables-Production/dp/B0DBDFQKVM/ref=sr_1_2?dib=eyJ2IjoiMSJ9.3g5Ms0XLG2ZMVc_qAl1S9PZ-3eqVxjpbCd2CCCep7nlvuwjnhwTWgeXUwjLyK7h66lMDmQRu-gIdKo1ax4k8pep5Xyf7vpjkKEASfE4jgcwMc3jtykf1lEGtNNDQPJ450MRt-0rmlyVfw4qYv6BVhTiNgIRqt652zfJrn5UztWXntNyyyT2ybeV6MWiX2ayzx2nTittqIuYfx9ZAT-Y9zNulhKloQUGDKAczyEZeybyscuC0Pa6slTeOJFj1VDwzfAGRBe6_blvkOmBhBMiVjP7k-y0YwDYkVpfp4Wjm9gA.Q7eO1owmVtplG__STvylO7PpI_a9CXH8HYCkr6MQPP8&dib_tag=se&keywords=urea+pesticide&qid=1732703240&sr=8-2",
            "price": 189
        },
        {
            "pesticide_name": "https://www.amazon.in/PANCHSHEEL-Potassium-Sulphate-Water-Soluble-Agriculture/dp/B09W5RF28B/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.mkaeP_8cs4MeBC8e4fsbV9vq5zHYFspNi3l87YSO4BBDdyYoID7LVAHIGr1UT7027I-5dstuymmJ803NbBokUTzCZ8nwY3EeB76MtZ6AuDCrTILSkdvVQrZhAkXnOiwGT6e7Nk10eZXvC94SV3f95Xb7YgAQ2-d-ySHbBC5aXAIBIj_Ag57YSbfu0ep_ScvusVUpfbeIJeDAWNQTXo4HPmv34fmQ9ZWI42KWCXVIwXCqJAmBa_CLvmDIuSmUJUi4LsTnRs4IyzaXNEUsPGSDLx8FTkd-UVm9k12aRVA_4_g.iRFkOZvT6ksO9pPpAKar7f44VDl9wJJpzdYL0cPeAeQ&dib_tag=se&keywords=Potassium+Sulfate+pesticide&qid=1732703453&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
            "image_url": "https://m.media-amazon.com/images/I/71qbJPFWKdL._SX522_.jpg",
            "buy_link": "https://www.amazon.in/PANCHSHEEL-Potassium-Sulphate-Water-Soluble-Agriculture/dp/B09W5RF28B/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.mkaeP_8cs4MeBC8e4fsbV9vq5zHYFspNi3l87YSO4BBDdyYoID7LVAHIGr1UT7027I-5dstuymmJ803NbBokUTzCZ8nwY3EeB76MtZ6AuDCrTILSkdvVQrZhAkXnOiwGT6e7Nk10eZXvC94SV3f95Xb7YgAQ2-d-ySHbBC5aXAIBIj_Ag57YSbfu0ep_ScvusVUpfbeIJeDAWNQTXo4HPmv34fmQ9ZWI42KWCXVIwXCqJAmBa_CLvmDIuSmUJUi4LsTnRs4IyzaXNEUsPGSDLx8FTkd-UVm9k12aRVA_4_g.iRFkOZvT6ksO9pPpAKar7f44VDl9wJJpzdYL0cPeAeQ&dib_tag=se&keywords=Potassium+Sulfate+pesticide&qid=1732703453&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
            "price": 279
        }
    ],
    "Nitrogen Deficiency": [
        {
            "pesticide_name": "PREPLE Urea Fertilizer Neem Coated Water Soluble for Vegetables, Flowers, Fruits Plants, Maximum Production, Ideal for Home, Terrace, and Outdoor Gardens",
            "image_url": "https://m.media-amazon.com/images/I/71l6y+z2OhL._SY500_.jpg",
            "buy_link": "https://www.amazon.in/PREPLE-Fertilizer-Soluble-Vegetables-Production/dp/B0DBDFQKVM/ref=sr_1_2?dib=eyJ2IjoiMSJ9.3g5Ms0XLG2ZMVc_qAl1S9PZ-3eqVxjpbCd2CCCep7nlvuwjnhwTWgeXUwjLyK7h66lMDmQRu-gIdKo1ax4k8pep5Xyf7vpjkKEASfE4jgcwMc3jtykf1lEGtNNDQPJ450MRt-0rmlyVfw4qYv6BVhTiNgIRqt652zfJrn5UztWXntNyyyT2ybeV6MWiX2ayzx2nTittqIuYfx9ZAT-Y9zNulhKloQUGDKAczyEZeybyscuC0Pa6slTeOJFj1VDwzfAGRBe6_blvkOmBhBMiVjP7k-y0YwDYkVpfp4Wjm9gA.Q7eO1owmVtplG__STvylO7PpI_a9CXH8HYCkr6MQPP8&dib_tag=se&keywords=urea+pesticide&qid=1732703240&sr=8-2",
            "price": 189
        },
        {
            "pesticide_name": "Bhumi N-32 (Urea Ammonium Nitrate) Liquid Fertilisers – 250 ML | Improve Crop Productivity & Reduce Nutrient Losses | Fast Absorption | Suitable for Variety of Crops | Enables Easy Mixing",
            "image_url": "https://m.media-amazon.com/images/I/51EABpOESZL._SX342_SY445_QL70_FMwebp_.jpg",
            "buy_link": "https://www.amazon.in/BHUMI-N-32-Fertiliser-Absorption-Performance/dp/B0DJP9Y4Z1/ref=sr_1_1?crid=37BP5SSOONSHM&dib=eyJ2IjoiMSJ9.W8ewr2KJtDfFzAR1Y3Y0Gjpv8fQPpnWH3p9COYsMf6cym79bg9cgOq8dPGtoMrwoyujGJdPDU0hCRVu-A44wW6O7hG5kRAU81nq2glqfHWvnJ9znikrIcpCNxEiVpI0HLNgU8yLoRTgj2_HcsWPcQhSN6wwMTunI-zcMD-kmGll-927Tz-phNORkQkmrx6Rqr2yfqYMTd5wiIZy1PUBwi5sLYZqvNbvJRSFtbYic9otYnkgRN531X5cAW2_YwP-3t82kVkFrwKYunN97koa_eLCrgRGt7hMEoh6XdwtOBCc.tVQL45ylnCWOhyxZyT055zSDvWod-5VgcyznnpoLoG8&dib_tag=se&keywords=Ammonium%2BNitrate%2Bpesticide&qid=1732703352&sprefix=ammonium%2Bnitrate%2Bpesticide%2Caps%2C1946&sr=8-1&th=1",
            "price": 295
        }
    ],
    "Potassium Deficiency": [
        {
            "pesticide_name": "https://www.amazon.in/PANCHSHEEL-Potassium-Sulphate-Water-Soluble-Agriculture/dp/B09W5RF28B/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.mkaeP_8cs4MeBC8e4fsbV9vq5zHYFspNi3l87YSO4BBDdyYoID7LVAHIGr1UT7027I-5dstuymmJ803NbBokUTzCZ8nwY3EeB76MtZ6AuDCrTILSkdvVQrZhAkXnOiwGT6e7Nk10eZXvC94SV3f95Xb7YgAQ2-d-ySHbBC5aXAIBIj_Ag57YSbfu0ep_ScvusVUpfbeIJeDAWNQTXo4HPmv34fmQ9ZWI42KWCXVIwXCqJAmBa_CLvmDIuSmUJUi4LsTnRs4IyzaXNEUsPGSDLx8FTkd-UVm9k12aRVA_4_g.iRFkOZvT6ksO9pPpAKar7f44VDl9wJJpzdYL0cPeAeQ&dib_tag=se&keywords=Potassium+Sulfate+pesticide&qid=1732703453&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
            "image_url": "https://m.media-amazon.com/images/I/71qbJPFWKdL._SX522_.jpg",
            "buy_link": "https://www.amazon.in/PANCHSHEEL-Potassium-Sulphate-Water-Soluble-Agriculture/dp/B09W5RF28B/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.mkaeP_8cs4MeBC8e4fsbV9vq5zHYFspNi3l87YSO4BBDdyYoID7LVAHIGr1UT7027I-5dstuymmJ803NbBokUTzCZ8nwY3EeB76MtZ6AuDCrTILSkdvVQrZhAkXnOiwGT6e7Nk10eZXvC94SV3f95Xb7YgAQ2-d-ySHbBC5aXAIBIj_Ag57YSbfu0ep_ScvusVUpfbeIJeDAWNQTXo4HPmv34fmQ9ZWI42KWCXVIwXCqJAmBa_CLvmDIuSmUJUi4LsTnRs4IyzaXNEUsPGSDLx8FTkd-UVm9k12aRVA_4_g.iRFkOZvT6ksO9pPpAKar7f44VDl9wJJpzdYL0cPeAeQ&dib_tag=se&keywords=Potassium+Sulfate+pesticide&qid=1732703453&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
            "price": 279
        },
        {
            "pesticide_name": "Potash (Muriate of Potash) - Premium Fertilizer for Plant Growth",
            "image_url": "https://m.media-amazon.com/images/I/61TSaoaOPbL._SY879_.jpg",
            "buy_link": "https://www.amazon.in/Potash-Muriate-Premium-Fertilizer-Growth/dp/B0DJQPZ9WZ/ref=sr_1_4?dib=eyJ2IjoiMSJ9.LLk1YT6ZMpJKj06QoIVqGm6aENID3NbxEbaetG5bhCSK8Nf1LQbwYuw15tL8xc-et0BcRChbMsOTOJyZZWI2rpjviljJDHp_j9z_AOnGt35VzKAi-tPZUbyGMIMlfHPrlJuEjQf1aYV3J4HK8t3avg9XgGLsHayagr_IlLFiYOTO__7MqveEkXJqWJF06gspY76GgH8NyaC_AlgeCihnT42DLfsDWhfmvSNrVyMS09s1VbqZHHKsFq4SRnqJKBYejKoxVr1acq7mpvgZxiJpReAJbOABrxJiqgc3A_3evFY.jCLfFbH4Nngfa2z8hLDYR6vDRoFETnGrgu2POFc1IZE&dib_tag=se&keywords=Muriate+of+Potash+pesticide&qid=1732703570&sr=8-4",
            "price": 3200
        }
    ]
 }
 
 
 if disease_name in pesticide_data:
    if pesticide_data[disease_name]:  # Check if the list for the disease is not empty
        print(f"Details for {disease_name}:")
        for i, product in enumerate(pesticide_data[disease_name], 1):
            st.markdown(f"\nOption {i}:")
            st.markdown(f"Pesticide Name: {product['pesticide_name']}")
            st.markdown(f"Price: ₹{product['price']}")  # Assuming the price is in INR
            st.markdown(f"Image URL: {product['image_url']}")
            st.markdown(f"Buy Link: {product['buy_link']}")
    else:
        print(f"No pesticides available for {disease_name}. Please check back later.")
 else:
    print("Invalid disease name. Please check and try again.")
    

# Load seed data from a JSON file
def load_seed_data():
    with open('seeds.json') as f:
        return json.load(f)

# Display seed grade information
def display_seed_info(seed_grade, seed_data):
    seed_info = seed_data.get(seed_grade, {})
    if seed_info:
        st.image(seed_info['image_url'], caption=f"{seed_grade} Image", use_column_width=True)
        st.write(f"[Buy {seed_grade}]({seed_info['buying_url']})")
    else:
        st.error("No information found for this grade.")
image = r'C:\Users\aradh\option 2\frontend\image.jpg'
# Define content for each page
if option == "Home":
    st.markdown("### Welcome to Dr. Tomato")
    st.markdown("Here, you can learn everything about tomatoes, the diseases they face, and how to grow them effectively.")

    # Image uploader
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    image = r'C:\Users\aradh\option 2\frontend\image.jpg'

    if uploaded_file is not None:
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        image=uploaded_image
        

    # Camera input
    camera_input = st.camera_input("Take a Photo")
    if camera_input is not None:
        captured_image = Image.open(camera_input)
        st.image(captured_image, caption="Captured Image", use_column_width=True)
        image=captured_image
disease_result=detect_disease(image)

if option == "Know About the Crop":
   st.markdown("### Know About the Tomato Crop")
   
   st.markdown("### Fertilizers")
   
   st.markdown("Enrich soil with compost or balanced fertilizer before planting")
    

    # Irrigation methods section
   st.markdown("### Irrigation Methods")
    
   st.markdown("Use drip irrigation to prevent waterlogging and nutrient leaching")
    

    # Soil types section
   st.markdown("### Soil Types")
   
   st.markdown("Use well-draining soil with a pH between 6.0 and 7.0 for optimal tomato growth")
    


if option == "Know About the Disease":
    if 'disease_result' in locals():
        # Show the detected disease
        disease_name = disease_result.get("disease", "Unknown")
        output = get_output_from_script(image)
        st.markdown(f"### Detected Disease: {disease_name}")
        st.markdown(f"**Percentage of the disease**:{output} ")
        
    
    else:
        st.markdown("Please upload or capture an image to detect the disease.")

if option == "Buy Pesticides":
    
 if 'disease_result' in locals():
    # Show the detected disease
    disease_name = disease_result.get("disease", "Unknown")
    st.markdown(f"### Detected Disease: {disease_name}")

    # Fetch detailed information about the disease
    pesticide_info = fetch_pesticide_info(disease_name) or {}  # Fallback to an empty dict if None

    # Check for errors in the response
    if pesticide_info.get("error"):
        st.error(f"Error: {pesticide_info['error']}")
    elif pesticide_info.get("pesticides"):
        # Display the pesticide information
        st.markdown("### Pesticide Information:")
        for i, pesticide in enumerate(pesticide_info["pesticides"], 1):
            st.markdown(f"**Option {i}:**")
            st.markdown(f"- **Name**: {pesticide['pesticide_name']}")
            st.markdown(f"- **Price**: ₹{pesticide['price']}")
            st.markdown(f"- [Buy Now]({pesticide['buy_link']})")
            st.image(pesticide["image_url"], width=300)
    else:
        st.info("No other pesticide information available for this disease.")
else:
    st.warning("Please upload or capture an image to detect the disease before buying pesticides.")





