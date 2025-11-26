import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image 

ext=pickle.load(open('Extra Trees.pkl','rb'))

st.title("Tree area cover type")

user_input = st.text_input('Input Features')

if user_input:
    user_input = user_input.split(',')
    features = np.array([user_input], dtype=np.float64)
    output = ext.predict(features).reshape(1, -1)

    # Create the cover type dictionary
    cover_type_dict = {
        1: {"name": "Spruce/Fir", "image": "img1.jpeg","info":"Spruce/Fir forests are cool-climate forests found in high mountains. They mainly contain spruce and fir trees, which stay green all year. These trees grow close together and create dense, dark forests. The area usually has cold temperatures, snow, and moist soil."},
        2: {"name": "Lodgepole Pine", "image": "img2.jpeg","info":"Lodgepole Pine forests are found in dry, high-altitude regions. The trees are tall, straight, and grow very close to each other. They can survive fires because their cones open only when heated. These forests grow well in sandy or rocky soil."},
        3: {"name": "Ponderosa Pine", "image": "img3.jpeg","info":"Ponderosa Pine forests grow in warm, dry areas. The trees are tall with thick, fire-resistant bark. These forests are more open, with plenty of sunlight reaching the ground. They are common in mountain slopes and dry valleys."},
        4: {"name": "Cottonwood/Willow", "image": "img4.jpeg","info":"Cottonwood/Willow vegetation grows near rivers, lakes, and wetlands. These trees need moist soil and plenty of water. Cottonwoods are tall with broad leaves, while willows have long, narrow leaves. This vegetation supports many birds and animals."},
        5: {"name": "Aspen", "image": "img5.jpeg","info":"Aspen forests are known for their bright yellow leaves in autumn. Aspens grow in groups called “clones,” meaning many trees are connected by the same root system. They prefer cool climates and grow quickly after forest fires. These forests are open and allow good sunlight."},
        6: {"name": "Douglas-fir", "image": "img6.jpeg","info":"Douglas-Fir forests are large, dense forests found in temperate regions. The trees are very tall and strong, often used for timber. They grow well in moist, cool climates. These forests have thick canopies and support many wildlife species."},
        7: {"name": "Krummholz", "image": "img7.jpeg","info":"Krummholz is a vegetation type found at the highest mountain elevations. Trees grow low, twisted, and bent because of strong winds, cold temperatures, and snow. It forms a transition zone between forest and treeless alpine tundra. Krummholz trees look stunted and shrub-like."}
    }

    # Convert the output to integer
    predicted_cover_type = int(output[0])
    cover_type_info = cover_type_dict.get(predicted_cover_type)

    if cover_type_info is not None:
        cover_type_name = cover_type_info["name"]
        cover_type_image_path = cover_type_info["image"]
        cover_info =cover_type_info["info"]

        # Display the cover type card
        col1, col2 = st.columns([2, 3])

        with col1:
            st.write("Predicted Cover Type:")
            st.write(f"<h1 style='font-size: 40px; font-weight: bold;'>{cover_type_name}</h1>", unsafe_allow_html=True)
            st.write(f"{cover_info}")

        with col2:
            cover_type_image = Image.open(cover_type_image_path)
            st.image(cover_type_image, caption=cover_type_name, use_container_width=True)
    else:
        st.write("Unable to make a prediction")

