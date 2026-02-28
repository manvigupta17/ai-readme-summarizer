import streamlit as st
from agent import generate_guided_tour

def extract_repo_name(input_text):
    if "github.com" in input_text:
        parts = input_text.split("github.com/")[-1]
        return parts.strip("/")
    return input_text.strip()

st.set_page_config(page_title="GitHub Guided Tour Agent", layout="wide")

st.title("GitHub Guided Tour Agent")
st.markdown("Enter a public GitHub repository in the format `owner/repo`")

repo_name = st.text_input(
    "Repository Name",
    placeholder="e.g. psf/requests or https://github.com/psf/requests"
)

if st.button("Generate Guided Tour"):
    if repo_name:
        with st.spinner("Analyzing repository..."):
            try:
                clean_repo = extract_repo_name(repo_name)
                result = generate_guided_tour(clean_repo)
                st.success("Analysis Complete ✅")
                st.markdown("## 📘 Guided Developer Tour")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a repository name.")