from pyscript import document, display

def generate_message(event):
    # Clear previous output
    output = document.getElementById("output")
    output.innerHTML = ""

    # Get values from inputs
    name = document.getElementById("name").value or "Unknown"
    age = document.getElementById("age").value or "N/A"
    school = document.getElementById("school").value or "N/A"
    birthdate = document.getElementById("birthdate").value or "N/A"

    # Multiline string with escape characters
    message = f"""😎Student Profile:
\t🗣️Name: {name}
\t🗓️Age: {age}
\t🚸School: {school}
\t🎂Birthday Date: {birthdate}

Welcome {name}! 👋🏼It's nice to meet you! \n\n📯NOTE: This information was gathered through input fields and displayed using a multiline string in Python via PyScript."""

    # Show result
    output.innerText = message

# Shortcut: directly assign the Python function as onclick handler
document.getElementById("generate-btn").onclick = generate_message

