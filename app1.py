from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.png"
project_images_dir = current_dir / "assets" / "project_images"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Austin Odey"
PAGE_ICON = ":wave:"
NAME = "Austino Nten Odey"
DESCRIPTION = """
Economist, Business Developer, Data Analyst, Leadership & Strategy Enthusiast
"""
EMAIL = "austino.n.odey@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/austino-odey-a0757a262/",
    "GitHub": "https://github.com/OdeyAustino",
    "Twitter": "https://x.com/ceegazz?s=21",
}
PROJECTS = {
    "🏆 Analytical Dashboards - Various Analysis": "https://github.com/OdeyAustino/ANALYTICAL-DASHBOARDS/tree/main",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        'Resume Sections',
        ['Introduction', 'Experience & Qualifications', 'Skills', 'Work History', 'Projects & Accomplishments'],
        icons=['person', 'briefcase', 'clipboard', 'building', 'star'],
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#00000d"},
            "icon": {"color": "white", "font-size": "22px"},
            "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "#555", "color": "white"},
            "nav-link-selected": {"background-color": "#007bff", "color": "white"},
        }
    )

# Function to apply custom styles to headers
def section_header(header):
    st.markdown(f"<h2 style='color:blue;'>{header}</h2>", unsafe_allow_html=True)

# --- CONTENT BASED ON SELECTION ---
if selected == "Introduction":
    st.image(profile_pic, width=60, use_container_width=True)
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(f"📫 {EMAIL}")
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write('\n')
    st.markdown(
        """
    <div style="display: flex; justify-content: space-between; width: 300px;">
        <a href="https://www.linkedin.com/in/austino-odey-a0757a262/" target="_blank" style="text-decoration: none; color: inherit;">
            <img src="https://img.icons8.com/color/50/000000/linkedin.png" width="40"/>
        </a>
        <a href="https://github.com/OdeyAustino" target="_blank" style="text-decoration: none; color: inherit;">
            <img src="https://img.icons8.com/color/50/000000/github.png" width="40"/>
        </a>
        <a href="https://x.com/ceegazz?s=21" target="_blank" style="text-decoration: none; color: inherit;">
            <img src="https://img.icons8.com/color/50/000000/twitter.png" width="40"/>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
    )

elif selected == "Experience & Qualifications":
    section_header("Experience & Qualifications")
    st.write(
        """
    - ✔️ BSc. Economics - Babcock University, Ogun, Nigeria
    - ✔️ Strong skills in business development, data analysis, and project management
    - ✔️ Experience in customer engagement, market research, and process optimization
    - ✔️ Leadership experience in student associations and professional roles
    - ✔️ Proven ability to analyze and interpret complex economic and business data
    """
    )

elif selected == "Skills":
    section_header("Skills")
    st.write(
        """
    - 📊 Data Analysis: Microsoft Excel, Microsoft Power BI, SQL, SPSS
    - 🤝 Business Development: Market Research, Strategy Development, Client Relationship Management
    - 📈 Project Management: Leadership, Process Optimization, Performance Tracking
    - 💡 Communication: Strong interpersonal, negotiation, and presentation skills
    - 🏆 Certifications: Soft-Skills Training (Jobberman), Microsoft Office, Customer Relationship Management, Project Management
    """
    )

elif selected == "Work History":
    section_header("Work History")
    
    # Job 1
    st.write("🚧", "**Business Developer/Data Analyst | Premium Pension Limited**")
    st.write("Jan 2023 – Nov 2023")
    st.write(
        """
    - Developed and executed strategic business development initiatives to drive revenue growth.
    - Conducted comprehensive market analysis to identify trends, opportunities, and competitive insights.
    - Managed and nurtured client relationships, ensuring high customer satisfaction and retention.
    - Implemented data-driven decision-making processes to optimize business operations and efficiency.
    - Led cross-functional collaboration to enhance service delivery and achieve organizational objectives.
    """
    )
    
    # Job 2
    st.write("🚧", "**Acquisition & Incubation Associate | Jumia**")
    st.write("Nov 2023 – Jan 2024")
    st.write(
        """
    - Spearheaded vendor acquisition strategies, significantly increasing the active vendor base.
    - Managed end-to-end onboarding processes for new vendors, ensuring seamless integration.
    - Provided data-backed insights to optimize vendor performance and sales conversion rates.
    - Established and maintained strong relationships with key stakeholders to foster long-term partnerships.
    """
    )
    
    # Leadership Roles Moved Here
    st.write("🚀", "**Welfare Director | Babcock University Students Association**")
    st.write("Mar 2021 – Apr 2022")
    st.write(
        """
    - Championed student welfare programs, ensuring access to essential support services.
    - Organized and led workshops, seminars, and events focused on mental health and career development.
    - Advocated for student needs, working closely with university administration to implement improvements.
    """
    )
    
    st.write("🚀", "**Assistant Social Director | Economics Students Association**")
    st.write("Mar 2019 – Mar 2020")
    st.write(
        """
    - Conceptualized and executed engaging social events to enhance student networking and community.
    - Coordinated logistics, budgeting, and promotions to maximize event impact and participation.
    - Strengthened partnerships with vendors and organizations to support student initiatives.
    """
    )

elif selected == "Projects & Accomplishments":
    section_header("Projects & Accomplishments")
    st.write("---")
    project_images = {
        "🏆 Analytical Dashboards - Various Analysis": "Netflix.png",
    }

    for project, details in PROJECTS.items():
        project_image = project_images_dir / project_images[project]
        st.write(f"### {project}")
        st.image(Image.open(project_image), width=300)
        st.write(f"[Link to project]({details})")

# --- PERSONALIZED MESSAGE ---
st.write('\n')
st.write("---")
st.write("Thank you for visiting my digital resume. Feel free to explore my projects and reach out to me through my social media channels!") 
