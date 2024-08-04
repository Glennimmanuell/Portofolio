from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "glenn-profile-pic.png"
ptpal = current_dir / "assets" / "PTPAL.jpg"
molca = current_dir / "assets" / "molca.jpg"
schneider = current_dir / "assets" / "schneider.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = " Glenn's Site"
PAGE_ICON = ":brain:"
NAME = "Glenn Immanuel Raditya Datau"
DESCRIPTION = """
AI Specialist, assisting enterprises by solving problem using modern technologies.
"""
EMAIL = "glennimmanuel8@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/glenn-immanuel-401b34276/",
    "YouTube": "https://www.youtube.com/channel/UCXIP7ADUyHjicUVRAxc0Jcw",
    "GitHub": "https://github.com/Glennimmanuell",
    "Projects & Activities": "https://www.linkedin.com/in/glenn-immanuel-401b34276/",
}
PROJECTS = {
    "🏆 Robot Light Follower - Robot that can follow the light": "https://www.youtube.com/watch?v=cgXTUwV5Y2k",
    "🏆 IoT Light Switch - Microcontroller that can control light switch through the internet": "https://www.youtube.com/watch?v=2k8PQAvXwSs&t=7s",
    "🏆 Finalist Noble UNESA - Developing SenseSight that can help blind people": "https://www.linkedin.com/in/glenn-immanuel-401b34276/details/projects/?profileUrn=urn%3Ali%3Afsd_profile%3AACoAAENxdEEBFopt_ClbddtXduHBAjytZkG0MbA",
    "🏆 AR for Medical Field - Developing AR for medical purpose": "https://www.linkedin.com/in/glenn-immanuel-401b34276/details/projects/?profileUrn=urn%3Ali%3Afsd_profile%3AACoAAENxdEEBFopt_ClbddtXduHBAjytZkG0MbA",
    "🏆 Chip Design - Create a simple basic processor using FPGA": "https://drive.google.com/drive/folders/1hzUBLrN1e880BIsoxmL4Rc-fcrIs00oC",
    "🏆 ToDo List Mobile App - Mobile Application for todo list": "https://github.com/Glennimmanuell/ToDo",
    "🏆 Smart Hospital App - This App can monitor whether the person in hospital did not used a mask, can monitor patients using several sensor in patients body": "https://github.com/Glennimmanuell/SmartHospital",
    "🏆 Autonomous Car - Using Ultrasonic sensor and Arduino to control the car": "https://drive.google.com/drive/folders/1i8Y3Yocn8Qp3SrFuj8tDWatOS3pYWUuU"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
ptpal = Image.open(ptpal)
molca = Image.open(molca)
schneider = Image.open(schneider)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📑​ Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📩​", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experiences")
st.write(
    """
- ✅​ 2 Years experience in AI technology design
- ✅​ Strong hands on experience and knowledge in Python and Computer Vision
- ✅​ Good understanding of Electrical Design and Programming Logic Controller (PLC)
- ✅​ Excellent team-player and displaying strong sense of initiative on tasks
- ✅​ Great understanding in AR/VR Development
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 💻 Programming: Python, C, C++, Java, Kotlin, C#, CSS, JavaScript
- ⚛️ Frameworks & Libraries: Tensorflow, PyTorch, Scikit-learn, keras, LangChain, openAI
- ⚡ Electrical Design Tools: ETAP, PLC Programming Software(TIA Portal, Machine Expert Basic), PCB Design(EasyEDA), ArduinoIDE
- 📟 Microcontrollers & Edge Devices: STM32, Arduino, Esp32, Raspberry Pi, Orange Pi, FPGA(Pynq Z2)
- 🧊 3D Design Tools: AutoCAD, Fushion360, Blender
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experiences")
st.write("---")

# --- JOB 1
cols1, cols2 = st.columns(2, gap="small")
with cols1:
    st.image(molca, width=230)
    st.write("AR Developer | Molca Technology")

with cols2:
    st.write("08/2024 - Present")
    st.write(
        """
    - ► Built Augmented Reality (AR) and Virtual Reality (VR) for Industry and Education purpose.
    - ► Integrate VR / AR with Internet of things, in case for Industry 5.0 that needs monitoring several machines.
    - ► Combine with Artificial Intelligence to made some chatbot inside of the VR, this purpose is for user experience in VR Application.
    - ► Work in team for developing any kind of VR/AR Application, i'm especially handled the Unity VR/AR developing process 
    """
    )

st.write("\n")
st.write("---")

# --- JOB 2
cols1, cols2 = st.columns(2, gap="small")
with cols1:
    st.image(ptpal, width=230)
    st.write("**AI Developer | PT. PAL**")

with cols2:
    st.write("06/2024 - 07/2024")
    st.write(
        """
    - ► Used Computer Vision and Artificial Intelligence to make a prediction for several machines and make a detection for QHSE implementation. I've just used PyTorch for handled deeplearning algorithm.
    - ► Work together in team for monitoring machines and detection using several sensors.
    - ► Redesigned data AI Algorithm and efficiency data pipeline. assisting 55% of the work of supervisors and engineers in monitoring QHSE and machines.  
    """
    )

st.write('\n')
st.write("---")

# --- JOB 3
cols1, cols2 = st.columns(2, gap="small")
with cols1:
    st.image(schneider, width=230)
    st.write("**Competition Comittee | Schneider**")

with cols2:
    st.write("11/2023 - 12/2023")
    st.write(
        """
    - ► Building an interesting event in a competition with the aim of ensuring that participants can enjoy the event.
    - ► Analyzed, documented, and reported participants survey results to improve the events. And we get 85% positive feedbacks.
    - ► Scheduling the competition and developing rules books for participants.
    - ► Led the Materials Division to created a software training for participants.
    """
    )


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
