import streamlit as st
import subprocess

st.title(" RAG Based AI Teaching Assistant")

query = st.text_input("Enter your question:")

if st.button("Get Answer"):

    if query:
        with st.spinner("Thinking... "):

            result = subprocess.run(
                ["python", "process_incoming.py"],
                input=query,        
                text=True,
                capture_output=True
            )

            # Show output
            if result.stdout:
                st.success("✅ Answer Generated")
                st.write(result.stdout)
            else:
                st.error("No output received")

            # Debug (optional)
            if result.stderr:
                st.error(result.stderr)

    else:
        st.warning("Please enter a question")