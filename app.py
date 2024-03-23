import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout = "wide") 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("D:\Demo\style\style.css")

lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_contact = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lt8ter7g.json")
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


image = Image.open("D:\Demo\img\image.jpg")
image2 = Image.open("D:\Demo\img\img2.jpg")
image3 = Image.open("D:\Demo\img\img3.jpg")
image4 = Image.open("D:\Demo\img\img2.jpg")
image5 = Image.open("D:\Demo\img\img2.jpg")
image6 = Image.open("D:\Demo\img\img2.jpg")
image7 = Image.open("D:\Demo\img\img2.jpg")
image8 = Image.open("D:\Demo\img\img2.jpg")

st.write("##")
# st.subheader("Hey Guys:wave:")
st.title("Deep Fake Detection 🕵️‍♂️")
st.write("""
         In today's digital era, the threat of deepfake technology is at large, posing significant risks.Our deepfake detection software offers a solution to accurately identify manipulated content
            - AI-Based Detection.
            - Facial Manipulation Recognition.
            - Detailed Reports and Visualizatio
         """)

st.write('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','News','Contact'],
        icons = ['person','code-slash','chat-left-text-fill'],
        orientation = 'horizontal'
    )

if selected == 'About':
    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We do")
        st.write("##")
        st.write(
                """
                Our deepfake detection software offers a solution to accurately identify manipulated content
                - AI-Based Detection.
                - Facial Manipulation Recognition.
                - Detailed Reports and Visualization.

                By combining AI-driven detection, facial recognition, and detailed reporting, our deepfake detection software ensures accurate identification of manipulated content. It empowers users to maintain the integrity of digital media and combat the spread of misinformation. 🚀
                """
            )    
        # st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
    with st.container():
        
        # st.header("My Projects")
        # st.write("##")
        # image_column, text_column = st.columns((1, 2))
        # with image_column:
        #     st.image(img_lottie_animation)
        # with text_column:
        #     st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        #     st.write(
        #         """
        #         Learn how to use Lottie Files in Streamlit!
        #         Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
        #         In this tutorial, I'll show you exactly how to do it
        #         """
        #     )
        #     st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
        st.divider() 
        st.subheader("System Architecture:")
        # uploaded_file = st.file_uploader("Upload CSV", type="mp4")
        # Load the image
        image = Image.open("D:\Demo\img\diagram.png")

        # Resize the image to a specific size (e.g., 600x400 pixels)
        resized_image = image.resize((1000, 1000))

        # Display the resized image
        st.image(resized_image) 

        # st.markdown("<p style='text-align: center;'><img src=./img/diagram.png></p>", unsafe_allow_html=True)

        st.write(""" 
                 
            1. Deepfake Detection System Design:

Designing a deepfake detection system involves several key components and considerations. Below is an outline of the functionalities and architecture for such a system:

1. **User Interface (UI)**:
   - The system should have a user-friendly interface for uploading videos.
   - It should provide feedback on the analysis results, indicating whether the video contains deepfake content.

2. **Automated Deepfake Detection**:
   - Utilize machine learning algorithms and computer vision techniques to automatically analyze uploaded videos for signs of deepfake manipulation.
   - Train deep learning models on a diverse dataset of both real and synthetic videos to recognize patterns indicative of deepfake content.
   - Use techniques such as facial recognition, lip-sync detection, and anomalous artifacts detection to identify potential deepfake alterations.

3. **Manual Flagging Mechanism**:
   - Allow users and administrators to manually flag videos suspected of containing deepfake content.
   - Implement a reporting system where users can provide feedback on flagged videos, helping to improve the system's accuracy.

4. **Integration with Moderation Tools**:
   - Integrate the deepfake detection system with moderation tools to facilitate the review and removal of flagged content.
   - Provide administrators with the ability to review flagged videos, take appropriate actions (e.g., removing or restricting access to flagged content), and provide feedback to improve the detection system.

5. **Scalability and Performance**:
   - Design the system to handle a large volume of video uploads efficiently.
   - Utilize cloud computing resources or distributed computing frameworks to ensure scalability and performance.

6. **Security and Privacy**:
   - Implement robust security measures to protect user data and prevent unauthorized access to uploaded videos.
   - Ensure compliance with privacy regulations by anonymizing user data and limiting access to sensitive information.

7. **Feedback Mechanism for Continuous Improvement**:
   - Collect feedback from users and administrators to continuously improve the deepfake detection algorithms.
   - Incorporate user feedback and labeled data into the training pipeline to enhance the system's accuracy over time.

8. **Education and Awareness**:
   - Provide educational resources and awareness campaigns to inform users about the risks associated with deepfake content.
   - Offer guidance on how to identify deepfake videos and mitigate their impact.

9. **Regulatory Compliance**:
   - Ensure compliance with relevant laws and regulations governing the detection and moderation of online content, including content moderation policies and data protection regulations.

By incorporating these functionalities and considerations into the design of the deepfake detection system, you can create a robust platform for identifying and mitigating the spread of deepfake content. Additionally, continuous monitoring and improvement are essential to adapt to evolving deepfake techniques and maintain the system's effectiveness over time.


        """)

if selected == "News":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns((1,2))
        with col5:
            st.image(image)
        with col6:
            st.subheader("Real or not? Top 5 ways to spot ‘deepfake’ videos and images")
            st.write(""" From Taylor Swift to Pope Francis, no one is immune to the AI fakery which is quickly becoming one of the biggest problems confronting us online.  """) 
            st.markdown("[Read Full News](https://www.hindustantimes.com/business/real-or-not-top-5-ways-to-spot-deepfake-videos-and-images-101711000519148.html)")
        col5, col6 = st.columns((1,2))
        with col5:
            st.image(image2)
        with col6:
            st.subheader("Italy PM Giorgia Meloni seeks $100k in damages over deepfake porn videos")
            st.write(""" Italy PM Giorgia Meloni's deep fake image is created by digitally superimposing the face of one person onto the body of another. The deepfake videos in question surfaced in 2022, prior to Meloni's appointment as Italy's Prime Minister.""") 
            st.markdown("[Read Full News](https://www.livemint.com/news/world/ai-misuse-italian-pm-giorgia-meloni-seeks-100k-in-damages-over-deepfake-porn-videos-11710998018576.html)")
        # with col5:
        #     st.image(image3)
        # with col6:
        #     st.subheader("Medanta Hospital flags Dr Naresh Trehan AI deepfake on obesity drug")
        #     st.write(""" Medanta Hospital reported a 'deepfake' video of Dr Naresh Trehan, leading to an FIR. The video spread misinformation on a weight loss drug. Cybercrime DCP Jain deactivated the video, initiating an investigation into voice manipulation and upcoming social media regulations.""") 
        #     st.markdown("[Read Full News](https://timesofindia.indiatimes.com/city/gurgaon/medanta-hospital-files-complaint-over-deepfake-video-featuring-dr-naresh-trehan-endorsing-obesity-drug/articleshow/108628878.cms)")
        # with col5:
        #     st.image(image4)
        # with col6:
        #     st.subheader("Italy PM Giorgia Meloni seeks $100k in damages over deepfake porn videos")
        #     st.write(""" Italy PM Giorgia Meloni's deep fake image is created by digitally superimposing the face of one person onto the body of another. The deepfake videos in question surfaced in 2022, prior to Meloni's appointment as Italy's Prime Minister.""") 
        #     st.markdown("[Read Full News](https://www.livemint.com/news/world/ai-misuse-italian-pm-giorgia-meloni-seeks-100k-in-damages-over-deepfake-porn-videos-11710998018576.html)")
        # with col5:
        #     st.image(image5)
        # with col6:
        #     st.subheader("Italy PM Giorgia Meloni seeks $100k in damages over deepfake porn videos")
        #     st.write(""" Italy PM Giorgia Meloni's deep fake image is created by digitally superimposing the face of one person onto the body of another. The deepfake videos in question surfaced in 2022, prior to Meloni's appointment as Italy's Prime Minister.""") 
        #     st.markdown("[Read Full News](https://www.livemint.com/news/world/ai-misuse-italian-pm-giorgia-meloni-seeks-100k-in-damages-over-deepfake-porn-videos-11710998018576.html)")
        # with col5:
        #     st.image(image6)
        # with col6:
        #     st.subheader("Italy PM Giorgia Meloni seeks $100k in damages over deepfake porn videos")
        #     st.write(""" Italy PM Giorgia Meloni's deep fake image is created by digitally superimposing the face of one person onto the body of another. The deepfake videos in question surfaced in 2022, prior to Meloni's appointment as Italy's Prime Minister.""") 
        #     st.markdown("[Read Full News](https://www.livemint.com/news/world/ai-misuse-italian-pm-giorgia-meloni-seeks-100k-in-damages-over-deepfake-porn-videos-11710998018576.html)")
        # with col5:
        #     st.image(image7)
        # with col6:
        #     st.subheader("Italy PM Giorgia Meloni seeks $100k in damages over deepfake porn videos")
        #     st.write(""" Italy PM Giorgia Meloni's deep fake image is created by digitally superimposing the face of one person onto the body of another. The deepfake videos in question surfaced in 2022, prior to Meloni's appointment as Italy's Prime Minister.""") 
        #     st.markdown("[Read Full News](https://www.livemint.com/news/world/ai-misuse-italian-pm-giorgia-meloni-seeks-100k-in-damages-over-deepfake-porn-videos-11710998018576.html)") 
        # with col5:
        #     st.image(image8)
        # with col6:
        #     st.subheader("Italy PM Giorgia Meloni seeks $100k in damages over deepfake porn videos")
        #     st.write(""" Italy PM Giorgia Meloni's deep fake image is created by digitally superimposing the face of one person onto the body of another. The deepfake videos in question surfaced in 2022, prior to Meloni's appointment as Italy's Prime Minister.""") 
        #     st.markdown("[Read Full News](https://www.livemint.com/news/world/ai-misuse-italian-pm-giorgia-meloni-seeks-100k-in-damages-over-deepfake-porn-videos-11710998018576.html)")   






if selected == "Contact":
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        contact_form = """ 
        <form action="https://getform.io/f/pbnvedmb" method="POST" enctype="multipart/form-data">
        <input type="email" placeholder="Enter your Email" name="email">
        <input type="text" placeholder="Enter your Name " name="name"><br>
        <input type="file" placeholder="Upload Video" name="file"><br>
        <button type="submit">Send</button>
        </form>

    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty() 



# uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

# # Check if a video file was uploaded
# if uploaded_video:
#     st.video(uploaded_video)
# else:
#     st.write("Please upload a video file (MP4, MOV, or AVI).")
        


# <form action="https://formsubmit.co/atharva333dalvi@gmail.com" method="POST">
#      <input type="hidden" name="_captcha" value = "false">
#      <input type="text" name="name" placeholder="Your Name" required>
#      <input type="text" name="email" placeholder="Your Email">
#      <textarea name = "message" placeholder = "Your Email" required></textarea>
#      <input type="file" name="photo" accept="image/*">
#      <button type = "submit">Submit</button>
#     </form>